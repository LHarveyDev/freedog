from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


LOCATION_CHOICES = (
    ("Large field", "Large field"),
    ("Small field", "Small field"),
    )
TIME_CHOICES = (
    ("9 AM", "9 AM"),
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("12 AM", "12 AM"),
    ("1 PM", "1 PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
)


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(
        max_length=20, choices=LOCATION_CHOICES, default="Large field")
    day = models.DateField(default=datetime.now)
    time = models.CharField(
        max_length=10, choices=TIME_CHOICES, default="9 AM")
    dogs = models.IntegerField(default=1)
    time_booked = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
