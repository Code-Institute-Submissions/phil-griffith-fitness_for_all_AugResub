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
        
        # check if memebership expiry is after today

        if profile.membership_level == 0:
            print("Free user, never paid for Full membership")
            return ret

        elif profile.membership_expiry_date > date.today():
            if profile.membership_fee_paid:
                print("Paid membership - Active")
                profile.save()
            else:
                print("UnPaid membership - InActive")
                return ret
        else:
            # If membership has expired, set profile membership level to free
            print("Paid membership - Expired")
            profile.membership_level = 0
            profile.expired_full_member = True
            profile.save()
            return ret

        
