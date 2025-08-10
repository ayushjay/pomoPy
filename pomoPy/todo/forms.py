from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TodoModel
from django.forms.widgets import DateTimeInput



class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'
    format = "%Y-%m-%dT%H:%M"

class TodoForm(forms.ModelForm):
        class Meta:
            model = TodoModel
            fields = ['title', 'description','due_date', 'completed']
            widgets = {
            'due_date': DateTimeInput(),
            }
            