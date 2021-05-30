from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def shop(request):
    """ View to return shop page """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'shop/shop.html', context)


def product_detail(request, product_id):
    """ View to display product detail """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)