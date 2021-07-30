from django.urls import path
from . import views

urlpatterns = [
    path('', views.workouts, name='workouts'),
    path('<int:workout_id>', views.workout, name='workout'),
    path('add/', views.add_workout, name='add_workout'),
    path('edit/<int:workout_id>/', views.edit_workout, name='edit_workout'),
    path('delete/', views.delete_workout, name='delete_workout'),
]