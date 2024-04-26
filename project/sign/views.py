from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.views.generic import CreateView

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

