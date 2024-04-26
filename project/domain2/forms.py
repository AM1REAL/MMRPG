from django import forms

from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'post_title', 'post_text']

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['response_text']


