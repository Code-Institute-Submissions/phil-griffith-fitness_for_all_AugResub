from decimal import Decimal
from Django.conf import settings


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0


    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context