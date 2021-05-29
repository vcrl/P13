from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelChoiceField
from django.contrib.auth.models import User
from .models import Service
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
import datetime

class NewService(forms.ModelForm):
    RACE_CHOICE = (
    ("Petite", "Petite"),
    ("Moyenne", "Moyenne"),
    ("Grande", "Grande"),
    )
    EXEC_CHOICE = (
        ("~ 5 min.", "~ 5 min."),
        ("~ 30 min.", "~ 30 min."),
        ("~ 1h00", "~ 1h00"),
        ("~ 1h30", "~ 1h30"),
        ("~ 2h00", "~ 2h00"),
        ("~ 2h +", "~ 2h +")
    )
    service = forms.CharField(max_length=255)
    prix = forms.DecimalField(max_digits=6, decimal_places=2)
    race = forms.ChoiceField(choices=RACE_CHOICE)
    duree = forms.ChoiceField(choices=EXEC_CHOICE)

    class Meta:
        fields = ('service', 'prix', 'race', 'duree')
        model = Service