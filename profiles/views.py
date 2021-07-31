from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import UserProfile
from .forms import UserProfileForm
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from allauth.account.views import SignupView
from allauth.exceptions import ImmediateHttpResponse
from allauth.account.utils import complete_signup
from allauth.account import app_settings
from datetime import datetime, timedelta
from fitness_for_all.decorators import full_membership_check
import json



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
@full_membership_check
def member_profiles(request):
    """ Display the user's profile. """

    profiles = UserProfile.objects.all()

    template = 'profiles/member_profiles.html'
    context = {
        'profiles': profiles,
    }

    return render(request, template, context)


def login_check(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if profile.membership_fee_due == 0:
        return redirect('home')
    else:
        return redirect(reverse('membership_checkout'))



class AccountSignupView(SignupView):
    # Signup View extended


    def form_valid(self, form):
        # By assigning the User to a property on the view, we allow subclasses
        # of SignupView to access the newly created User instance

        self.user = form.save(self.request)
        try:          
            return complete_signup(
                self.request,
                self.user,
                app_settings.EMAIL_VERIFICATION,
                self.get_success_url(),
            )
        except ImmediateHttpResponse as e:
            return e.response

        form_data = {
            'first_name': self.request.POST['first_name'],
        }
        return redirect('account_signup_view')

       
account_signup_view = AccountSignupView.as_view()


def update_membership(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    membership_selected = int(request.POST['membership_type'])


    if membership_selected == 30:
        fee_due = 19.99
        print("30 days")
    elif membership_selected == 180:
        fee_due = 99.99
        print("180 days")
    else:
        fee_due = 159.99
        print("365 days")
    profile.membership_fee_due = fee_due
    profile.membership_level_selected = membership_selected
    profile.save()
    return redirect(reverse('login_check'))






