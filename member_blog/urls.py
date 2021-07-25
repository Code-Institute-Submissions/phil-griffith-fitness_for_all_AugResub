from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_blog, name='member_blog'),
    path('add_blog', views.add_blog, name='add_blog'),
]
