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
        
        # check if memebership status 

        # check for free user
        if profile.membership_level == 0:
            print("Free user, never paid for Full membership")
            return ret

        # check for full member
        elif profile.membership_expiry_date > date.today():
            # check if payment has been made
            if profile.membership_fee_due == 0:
                print("Paid membership - Active")
                profile.full_member = True
                profile.expired_full_member = False
                profile.save()
            else:
                print("UnPaid membership - InActive")
                return ret
        else:
            # If membership has expired set expired full member flag to true
            print("Paid membership - Expired")
            profile.expired_full_member = True
            profile.full_member = False
            profile.save()
            return ret

        
