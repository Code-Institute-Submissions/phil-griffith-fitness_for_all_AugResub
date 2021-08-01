from allauth.account.adapter import DefaultAccountAdapter
from django.http import HttpResponseRedirect
from django.urls import reverse


# if account is inactive, redirect to shop page
class ProfileAppAccountAdapter(DefaultAccountAdapter):
    def respond_user_inactive(self, request, user):
        return HttpResponseRedirect(reverse("shop"))
        
