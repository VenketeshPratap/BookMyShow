# bookmyshow/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),       # Users endpoints (register, login, etc.)
    path('api/events/', include('events.urls')),     # Events endpoints (create, list, etc.)
    path('api/bookings/', include('bookings.urls')), # Bookings endpoints (book, cancel, etc.)
]
