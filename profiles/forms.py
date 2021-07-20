from django import forms
from allauth.account.forms import SignupForm
from .models import UserProfile
from datetime import datetime, timedelta

# Code taken from Code Institute Boutique Ado project



class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user',)
        # https://stackoverflow.com/questions/8761106/how-can-i-get-a-textarea-from-modelmodelform
        widgets = {
            'goal': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
        

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Postal Code',
            'default_country': 'Country',
            'goal': 'Goal',
            'profile_pic': 'Profile Pic',
            'membership_level_selected': 'Membership Level',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        
        for field in self.fields:
            if field not in ('default_country', 'date_joined', 'membership_expiry_date'):
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ''
            self.fields[field].label = False


# https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/
class CustomSignupForm(SignupForm):

    MEMBERSHIP_LEVEL_SELECTED = [
        (0, 'Free'),
        (30, 'Full - 30 days (£19.99)'),
        (180, 'Full - 6 months (£99.99)'),
        (365, 'Full - 1 year (£160)'),
    ]

    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    membership_level_selected = forms.ChoiceField(choices=(MEMBERSHIP_LEVEL_SELECTED),  label='Membership Level')

    def signup(self, request, user):
        profile = models.UserProfile.objects.get_or_create(user=user)
        profile.save()
