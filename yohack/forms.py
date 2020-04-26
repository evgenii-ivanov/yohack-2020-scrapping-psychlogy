from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserCharacteristics

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields  = ['username', 'first_name', 'last_name', 'email']


class UserCharacteristicsUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = UserCharacteristics
        fields  = [
            'sphere',
            'b5_consc',
            'b5_extr',
            'b5_open',
            'b5_agree',
            'b5_neur',
            'is_startuper',
            'twitter_username',
            'instagram_username',
            'money'
        ]