# events/urls.py
from django.urls import path
from .views import EventCreateView, EventListView

urlpatterns = [
    path('create-event/', EventCreateView.as_view(), name='create-event'),
    path('events/', EventListView.as_view(), name='events'),
]
