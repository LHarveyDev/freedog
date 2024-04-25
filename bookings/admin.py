from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "day",
        "time",
        "location",  # Display the location field
        "price",  # Display the price field
        "dogs",
        "time_booked"
    )


admin.site.register(Booking, BookingAdmin)
