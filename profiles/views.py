from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import UserProfile
from .forms import UserProfileForm
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)

@login_required
def edit_profile(request):
    """ Edit the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('personal_details'))
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
            return redirect(reverse('personal_details'))
    else:
        form = UserProfileForm(instance=profile)
        
    orders = profile.orders.all()
    form = UserProfileForm(instance=profile)

    template = 'profiles/edit_profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def personal_details(request):
    """ Display the user's full profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/personal_details.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def order_history(request):
    """ Display the user's full profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    template = 'profiles/order_history.html'
    context = {
        'profile': profile,
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def member_profiles(request):
    """ Display the user's profile. """

    profiles = UserProfile.objects.all()



    template = 'profiles/member_profiles.html'
    context = {
        'profiles': profiles,
    }

    return render(request, template, context)



