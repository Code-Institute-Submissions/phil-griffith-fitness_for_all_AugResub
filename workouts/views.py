from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Workouts, Category

# Create your views here.


def workouts(request):
    """ View to return workouts page """

    # code taken from Code Institute Boutique Ado walk through project
    workouts = Workouts.objects.all()    
    categories = None
    sort = None
    direction = None
    category = "all_workouts"

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                workouts = workouts.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            workouts = workouts.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            category = categories[0]
            
            
            workouts = workouts.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
       
    current_sorting = f'{sort}'
    context = {
        'workouts': workouts,
        'categories': categories,
        'category': category,
        'current_sorting': current_sorting,
    }

    return render(request, 'workouts/workouts.html', context)


def workout(request, workout_id):
    """ View to display workout video """

    workout = get_object_or_404(Workouts, pk=workout_id)

    context = {
        'workout': workout,
    }

    return render(request, 'workouts/workout.html', context)






