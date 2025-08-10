from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TodoModel
from django.forms.widgets import DateTimeInput



class RegisterForm(UserCreationForm):
    """Form to register User"""

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class DateInput(forms.DateInput):
    input_type = 'date'

class TodoForm(forms.Form):
        title = forms.CharField(max_length=60)
        description = forms.Textarea()
        due_date = forms.DateTimeField(
            widget=DateTimeInput(attrs={'type': 'datetime-local'})
        )