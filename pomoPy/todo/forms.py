from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TodoModel



class RegisterForm(UserCreationForm):
    """Form to register User"""

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class TodoForm(forms.Form):
    class Meta:
        model = TodoModel
        fields = "__all__"



