# bookings/urls.py
from django.urls import path
from .views import BookingCreateView, BookingListView, BookingCancelView

urlpatterns = [
    path('book-ticket/', BookingCreateView.as_view(), name='book-ticket'),
    path('my-bookings/', BookingListView.as_view(), name='my-bookings'),
    path('cancel-booking/<int:pk>/', BookingCancelView.as_view(), name='cancel-booking'),
]
