from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Workouts, Category
from .forms import WorkoutsForm



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


@login_required
def workout(request, workout_id):
    """ View to display workout video """

    workout = get_object_or_404(Workouts, pk=workout_id)

    context = {
        'workout': workout,
    }

    return render(request, 'workouts/workout.html', context)


@login_required
def add_workout(request):
    """ Add a workout  """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = WorkoutsForm(request.POST, request.FILES)
        if form.is_valid():
            workout = form.save()
            messages.success(request, 'Successfully added workout!')
            return redirect(reverse('workout', args=[workout.id]))
        else:
            messages.error(request, 'Failed to add workout. Please ensure the form is valid.')
    else:
        form = WorkoutsForm()
        
    template = 'workouts/add_workout.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_workout(request, workout_id):
    """ Edit a workout """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('workouts'))

    workout = get_object_or_404(Workouts, pk=workout_id)
    if request.method == 'POST':
        form = WorkoutsForm(request.POST, request.FILES, instance=workout)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated workout!')
            return redirect(reverse('workout', args=[workout.id]))
        else:
            messages.error(request, 'Failed to update workout. Please ensure the form is valid.')
    else:
        form = WorkoutsForm(instance=workout)
        messages.info(request, f'You are editing {workout.name}')

    template = 'workouts/edit_workout.html'
    context = {
        'form': form,
        'workout': workout,
    }

    return render(request, template, context)


@login_required
def delete_workout(request, workout_id):
    """ Delete a workout  """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('workouts'))
        
    workout = get_object_or_404(Workouts, pk=workout_id)
    workout.delete()
    messages.success(request, 'Workout deleted!')
    return redirect(reverse('workouts'))






