from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product
from profiles.models import UserProfile


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    delivery = 0
    discount = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })
    # Check for full member and apply discount
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        if profile.full_member:
            discount = total / 10
        else:
            discount = 0
                       
    delivery = settings.STANDARD_DELIVERY_CHARGE

    grand_total = delivery + total - discount

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
