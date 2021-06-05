from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "You have not added anything to your backet yet.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Il74cBXqliCtNkZf0M2GIohN0M8WjDz5KQALN76iak9I0M0mOZKxHFWPVI5WtAXZWOuoSPKd6IfhItWQ2VHSTBi00YbSLjLvB',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

