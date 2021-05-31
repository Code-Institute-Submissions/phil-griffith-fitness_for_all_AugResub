from django.urls import path
from . import views

urlpatterns = [
    path('', views.workouts, name='workouts'),
    path('<workout_id>', views.workout, name='workout'),
]