from django.shortcuts import render, redirect
from .models import Booking
from django.contrib import messages
from datetime import datetime, timedelta


def index(request):
    return render(request, "home/index.html")


def booking(request):
    weekdays = validWeekday(31)

    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        location = request.POST.get('location')
        day = request.POST.get('day')
        dogs = request.POST.get('dogs')

        if location is None:
            messages.success(request, "Please Select a Field")
            return redirect('booking')

        request.session['day'] = day
        request.session['location'] = location
        request.session['dogs'] = dogs
        return redirect('bookingSubmit')

    return render(request, 'bookings/bookings.html', {
            'weekdays': weekdays,
            'validateWeekdays': validateWeekdays,
        })


def bookingSubmit(request):
    user = request.user
    times = [
        '9 AM', '10 AM', '11 AM', '12 AM', '1 PM', '2 PM', '3 PM'
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=31)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    location = request.session.get('location')
    dogs = request.session.get('dogs')

    hour = checkTime(location, times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if location is not None:
            if day <= maxDate and day >= minDate:
                if date == 'Wednesday' or date == 'Thursday' or date == 'Friday' or date == 'Saturday' or date == 'Sunday':
                    if Booking.objects.filter(day=day).count() < 11:
                        if Booking.objects.filter(location=location, day=day, dogs=dogs, time=time).count() < 1:
                            BookingForm = Booking.objects.create(
                                user=user,
                                location=location,
                                day=day,
                                dogs=dogs,
                                time=time,
                            )
                            messages.success(request, "Your Booking has been Saved!")
                            return redirect('index')
                        else:
                            messages.success(
                                request, "The selected date is unavailable")
                    else:
                        messages.success(
                            request, "The selected day is not available")
                else:
                    messages.success(
                        request, "The selected date is not available")
            else:
                messages.success(
                    request, "Selected date not in the correct time period")
        else:
            messages.success(
                request, "Please select a Field")

    return render(
        request, 'bookings/bookingSubmit.html', {'times': hour, })


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def validWeekday(days):
    # Loop days you want in the next 31 days:
    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Wednesday' or y == 'Thursday' or y == 'Friday' or y == 'Saturday' or y == 'Sunday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Booking.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays


def checkTime(location, times, day):
    # Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Booking.objects.filter(location=location, day=day, time=k).count() < 1:
            x.append(k)
    return x


def booking_list(request):
    current_booking = None
    if request.user.is_authenticated:
        latest_booking = Booking.objects.filter(user=request.user).order_by('-time_booked').first()
        if latest_booking:
            current_booking = latest_booking

    return render(request, 'bookings/booking_list.html', {
        'current_booking': current_booking})
