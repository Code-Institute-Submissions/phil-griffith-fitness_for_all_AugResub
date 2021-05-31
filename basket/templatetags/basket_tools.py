
from django import template

# code taken from Code Institute Boutique Ado project
register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
