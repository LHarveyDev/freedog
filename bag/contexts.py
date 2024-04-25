from decimal import Decimal
from django.conf import settings
from products.models import Product


def bag_contents(request):
    bag = request.session.get('bag', {})
    bag_items = []
    total = 0

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'grand_total': grand_total,
    }

    return context
