from allauth.account.auth_backends import ModelBackend
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from profiles.models import UserProfile
from allauth.account.utils import filter_users_by_username
from datetime import date


class MyAuthenticationBackend(ModelBackend):

    def authenticate(self, request, **credentials):
        username = credentials.get("username")
        
        try:
            user = filter_users_by_username(username).get()

            ret = self._authenticate_by_username(**credentials)   
            profile = get_object_or_404(UserProfile, user=user)

            if user.is_superuser:
                return ret

            else:        
                # check if memebership status

                # check for free user
                if profile.membership_level == 0:

                    return ret

                # check for full member
                elif profile.membership_expiry_date > date.today():
                    # check if payment has been made
                    if profile.membership_fee_due == 0:

                        profile.full_member = True
                        profile.expired_full_member = False
                        profile.save()
                    else:

                        return ret
                else:
                    # If membership has expired set expired
                    # full member flag to true

                    profile.expired_full_member = True
                    profile.full_member = False
                    profile.save()
                    return ret
        except User.DoesNotExist:
            return None

