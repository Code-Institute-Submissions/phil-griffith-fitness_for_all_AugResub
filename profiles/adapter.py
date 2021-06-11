from allauth.account.adapter import DefaultAccountAdapter
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


class ProfileAppAccountAdapter(DefaultAccountAdapter):
    def respond_user_inactive(self, request, user):
        return HttpResponseRedirect(reverse("shop"))
        
