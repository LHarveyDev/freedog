from django.contrib import admin
from .models import Booking

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "day",
        "time",
        "location",
        "dogs",
        "time_booked"
    )


admin.site.register(Booking, BookingAdmin)
