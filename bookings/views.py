from django.shortcuts import render, redirect
from .models import Booking
from django.contrib import messages
from datetime import datetime


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

        # Check if the selected location is available
        if Booking.objects.filter(
                day=day, time=time, location=location).exists():
            messages.error(request, "The selected field is not available.")
            return redirect('booking')

        # Create the booking
        Booking.objects.create(
            location=location,
            day=day,
            time=time,
        )

        messages.success(request, "Booking successful!")
        return redirect('booking')

    # Get all existing bookings
    existing_bookings = Booking.objects.all()

    # Extract booked days and times
    booked_days = set(booking.day for booking in existing_bookings)
    booked_times = set(booking.time for booking in existing_bookings)

    # Get all available days and times
    all_days = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday']
    all_times = ['9 AM', '10 AM', '11 AM', '12 AM', '1 PM', '2 PM', '3 PM']

    # Exclude booked days and times from available options
    available_days = [day for day in all_days if day not in booked_days]
    available_times = [time for time in all_times if time not in booked_times]

    return render(request, 'bookings/bookings.html', {
        'available_days': available_days,
        'available_times': available_times
    })
