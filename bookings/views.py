# bookings/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # Make sure this is imported
from .models import Booking
from .serializers import BookingSerializer
from events.models import Event
from rest_framework import serializers  # Import for validation error handling

class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        event = serializer.validated_data['event']
        if event.available_tickets > 0:
            event.available_tickets -= 1
            event.save()
            serializer.save(user=self.request.user)
        else:
            raise BookingSerializer.validate("No tickets available for this event.")

class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class BookingCancelView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        booking = self.get_object()
        event = booking.event
        event.available_tickets += 1  # Refund ticket to event
        event.save()
        return super().delete(request, *args, **kwargs)
