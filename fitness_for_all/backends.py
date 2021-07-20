from allauth.account.auth_backends import AuthenticationBackend
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from profiles.models import UserProfile
from allauth.account.utils import filter_users_by_email, filter_users_by_username
from datetime import datetime, timedelta
from datetime import date

class MyAuthenticationBackend(AuthenticationBackend):

    def authenticate(self, request, **credentials):
        username = credentials.get("username")
        user = filter_users_by_username(username).get()
        print(user)

        ret = self._authenticate_by_username(**credentials)   
        profile = get_object_or_404(UserProfile, user=user)
        print(profile.days_added)
        
        # check if memebership expiry is after today

        if profile.membership_expiry_date > date.today():
            print(profile.days_added)
            return ret

        else:
            # If membership has expired, set account to inactive
            ret.is_active = False
            return ret

        
