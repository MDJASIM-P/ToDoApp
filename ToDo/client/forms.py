from django import forms
from .models import *


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
    class Meta:
        model= User
        fields = ["first_name","last_name", "email", "username", "password1", "password2"]
class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget= forms.PasswordInput())

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = ['event', 'date', 'time']
        widgets = {
            'date':forms.DateInput(attrs={'type':'date'}),
            'time':forms.TimeInput(attrs={'type':'time'})
        }