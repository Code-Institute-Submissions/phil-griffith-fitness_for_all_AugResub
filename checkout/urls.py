from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
    path('membership_checkout', views.membership_checkout, name='membership_checkout'),
    path('membership_checkout_success', views.membership_checkout_success, name='membership_checkout_success'),
]
