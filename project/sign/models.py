from django.db import models
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='Ник')

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
