from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelChoiceField
from django.contrib.auth.models import User
from .models import RDV
from clients.models import Client
from services.models import Service
from employes.models import Employee
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
import datetime

class NewRDV(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), initial=0)
    service = forms.ModelMultipleChoiceField(queryset=Service.objects.all(), initial=0)
    date =  forms.DateTimeField(
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
 #forms.DateField(initial=datetime.date.today)
    comment = forms.CharField(max_length=255, widget=forms.Textarea)
    toiletteur = forms.ModelChoiceField(queryset=Employee.objects.all(), initial=0)
    
    class Meta:
        fields = ('client', 'service', 'date', 'comment', 'toiletteur')
        model = RDV