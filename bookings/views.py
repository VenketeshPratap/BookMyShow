# bookings/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # Make sure this is imported
from django.db import transaction
from django.db.models import F, Prefetch
from .models import Booking
from .serializers import BookingSerializer
from events.models import Event
from rest_framework import serializers  # Import for validation error handling

class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def perform_create(self, serializer):
        event = serializer.validated_data['event']
        # Lock row for update to prevent race conditions and overselling
        event_locked = Event.objects.select_for_update().get(pk=event.pk)
        if event_locked.available_tickets <= 0:
            raise serializers.ValidationError("No tickets available for this event.")
        event_locked.available_tickets = F('available_tickets') - 1
        event_locked.save()
        # Refresh to get the actual decremented integer value
        event_locked.refresh_from_db(fields=['available_tickets'])
        serializer.save(user=self.request.user, event=event_locked)

class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Optimize to prevent N+1 on event and user
        return (
            Booking.objects
            .filter(user=self.request.user)
            .select_related('event', 'user')
        )

class BookingCancelView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        booking = self.get_object()
        # Ensure users can only cancel their own bookings
        if booking.user_id != request.user.id:
            return Response({"detail": "Not allowed"}, status=status.HTTP_403_FORBIDDEN)
        event = Event.objects.select_for_update().get(pk=booking.event_id)
        event.available_tickets = F('available_tickets') + 1
        event.save()
        response = super().delete(request, *args, **kwargs)
        return response
