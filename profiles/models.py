from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta


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
    membership_expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.membership_expiry_date is None:
                self.membership_expiry_date = self.date_joined + timedelta(days=365)
        super(UserProfile, self).save(*args, **kwargs)
        


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
