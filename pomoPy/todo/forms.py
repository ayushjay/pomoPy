from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TodoM

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]


class TodoForm(forms.Form):
    class Meta:
        model = TodoM
        fields = "__all__"



