from django.shortcuts import render, redirect
from .models import Booking
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, "index.html", {})


def booking(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        day = request.POST.get('day')
        time = request.POST.get('time')

        # Check if location, day, and time are selected
        if not (location and day and time):
            messages.error(request, "Please fill out all fields.")
            return redirect('booking')

        # Check if the selected time slot is available
        if Booking.objects.filter(day=day, time=time).exists():
            messages.error(request, "The selected time slot is not available.")
            return redirect('booking')

        # Create the booking
        Booking.objects.create(
            location=location,
            day=day,
            time=time,
        )

        messages.success(request, "Booking successful!")
        return redirect('booking')

    return render(request, 'bookings/bookings.html')
