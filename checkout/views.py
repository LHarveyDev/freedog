from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from bookings.models import Booking  # Import Booking model

import stripe

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Fetch booking information from the database
    booking_id = request.session.get('booking_id')
    if booking_id:
        booking = Booking.objects.get(pk=booking_id)
    else:
        messages.error(request, "No booking found.")
        return redirect(reverse('index'))  # Redirect to index page if no booking found

    # Prepare data for Stripe payment
    stripe_total = int(booking.price * 100)  # Convert price to cents for Stripe
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'booking': booking,  # Pass booking object to template
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
