from django import forms
from django.contrib.auth.models import User
from . import models


class signup_form(forms.ModelForm):
    class Meta:
        model = models.users
        fields = [
            'f_name',
            'l_name',
            'gender',
            'age',
            'contact',
            'lang_fluent_in',
            'disability'
        ]


class user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
