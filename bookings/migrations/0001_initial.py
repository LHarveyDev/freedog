# Generated by Django 3.2.25 on 2024-04-20 12:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('Large field', 'Large field'), ('Small field', 'Small field')], default='Large field', max_length=20)),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('9 AM', '9 AM'), ('10 AM', '10 AM'), ('11 AM', '11 AM'), ('12 AM', '12 AM'), ('1 PM', '1 PM'), ('2 PM', '2 PM'), ('3 PM', '3 PM')], default='9 AM', max_length=10)),
                ('dogs', models.IntegerField(default=1)),
                ('time_booked', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
