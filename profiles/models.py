from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta
from allauth.account.signals import user_signed_up
from allauth.account.auth_backends import AuthenticationBackend



from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
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
    date_joined = models.DateField(default=datetime.now)
    days_added = models.IntegerField(blank=True, null=True)
    membership_expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)
        


    @receiver(user_signed_up)
    def populate_profile(request, user, **kwargs):

        profile = UserProfile()
        membership_length = int(request.POST.get("days_added"))
        profile.user = user
        profile.first_name = user.first_name
        profile.last_name = user.last_name
        profile.days_added = membership_length
        profile.membership_expiry_date = datetime.now() + timedelta(days=membership_length)

        profile.save()   





