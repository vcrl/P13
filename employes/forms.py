from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelChoiceField
from django.contrib.auth.models import User
from .models import Employee
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
import datetime

class NewEmployee(forms.ModelForm):
    prenom = forms.CharField(max_length=254)
    nom = forms.CharField(max_length=254)
    adresse = forms.CharField(max_length=254)
    num = forms.CharField(max_length=254)
    joined = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        ),
    )

    class Meta:
        fields = ('prenom', "nom", "adresse", "num", "joined")
        model = Employee