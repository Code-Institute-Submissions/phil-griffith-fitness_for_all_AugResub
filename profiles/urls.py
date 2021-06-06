from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('member_profiles/', views.member_profiles, name='member_profiles'),
]