# bookings/serializers.py
from rest_framework import serializers
from .models import Booking
from events.models import Event

class BookingSerializer(serializers.ModelSerializer):
    event_title = serializers.ReadOnlyField(source='event.title')
    user_email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Booking
        fields = ['id', 'user', 'event', 'event_title', 'user_email', 'booking_date']
        read_only_fields = ['user', 'booking_date']

    def validate(self, data):
        event = data.get('event')
        if event.available_tickets <= 0:
            raise serializers.ValidationError("No tickets available for this event.")
        return data
