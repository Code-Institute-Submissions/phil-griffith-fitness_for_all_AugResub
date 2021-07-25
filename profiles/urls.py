from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('member_profiles/', views.member_profiles, name='member_profiles'),
    path('order_history/', views.order_history, name='order_history'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('personal_details/', views.personal_details, name='personal_details'),
    path('account_signup_view', views.account_signup_view, name='account_signup_view'),
    path('login_check', views.login_check, name='login_check'),
    path('update_membership', views.update_membership, name='update_membership'),
]