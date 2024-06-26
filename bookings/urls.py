from django.urls import path
from . import views

urlpatterns = [
    path('bookings', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    path('index', views.index, name='index'),
    path('booking-list', views.booking_list, name='booking_list'),
]
