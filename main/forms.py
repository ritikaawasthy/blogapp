from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Blog, ExtendedUser
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']

class ExtendedUserForm(ModelForm):
    class Meta:
        model= ExtendedUser
        fields=['user']

class BlogForm(ModelForm):
    class Meta:
        model= Blog
        fields=['user', 'title', 'name', 'content', 'tag', 'image']
