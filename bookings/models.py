from django.contrib.auth.models import User
from django.db import models


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    dogs = models.IntegerField(default=1)
    booking_date = models.DateField()
    booking_time = models.TimeField()
