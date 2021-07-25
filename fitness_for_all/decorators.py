from django.shortcuts import render, redirect, reverse, get_object_or_404
from profiles.models import UserProfile

# https://stackoverflow.com/questions/63434014/how-to-use-to-make-custom-decorators-in-django
# https://micropyramid.medium.com/custom-decorators-to-check-user-roles-and-permissions-in-django-ece6b8a98d9d

def is_free_member(self):
    if self.membership_level == 0:
        return True
    else:
        return False


def is_expired_full_member(self):
    if self.expired_full_member:
        return True
    else:
        return False


def full_membership_check(view_func):
    def wrapper_func(request, *args, **kwargs):
        profile = get_object_or_404(UserProfile, user=request.user)
        if is_free_member(profile):
            print("Non Full member trying to access..")
            return redirect('home')
            
        elif is_expired_full_member(profile):
            print("Expired Full member trying to access..")
            return redirect('home')         
        else:
            print("Full Member accessing")
            return view_func(request, *args, **kwargs)
    return wrapper_func


    

