from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta
from allauth.account.signals import user_signed_up
from allauth.account.auth_backends import AuthenticationBackend
from django.shortcuts import render, redirect, reverse, get_object_or_404



from django_countries.fields import CountryField



class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=3, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    goal = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    date_joined = models.DateField(blank=True, default=datetime.now)
    membership_expiry_date = models.DateField(blank=True, null=True)
    full_member = models.BooleanField(blank=True, default=False)
    expired_full_member = models.BooleanField(blank=True, default=False)
    membership_level_selected = models.IntegerField(blank=True, default=0)
    membership_level = models.IntegerField(blank=True, default=0)
    membership_fee_due = models.FloatField(blank=True, default=0)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)
        

    # @receiver(user_signed_up)
    # def populate_profile(request, user, **kwargs):

    #     profile = get_object_or_404(UserProfile, user=request.user)
    #     membership_length = int(request.POST.get("membership_level_selected"))
    #     profile.user = user
    #     profile.membership_level_selected = membership_length
    #     if membership_length == 30:
    #         profile.membership_fee_due = 19.99
    #     elif membership_length == 180:
    #         profile.membership_fee_due = 99.99
    #     elif membership_length == 365:
    #         profile.membership_fee_due = 159.99
    #     profile.membership_expiry_date = datetime.now() + timedelta(days=membership_length)

    #     profile.save()   


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()





