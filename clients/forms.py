from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelChoiceField
from django.contrib.auth.models import User
from .models import Client, Chien, Race
from employes.models import Employee
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
import datetime

class NewClient(forms.ModelForm):
    prenom = forms.CharField(max_length=254)
    nom = forms.CharField(max_length=254)
    adresse = forms.CharField(max_length=254)
    num = forms.CharField(max_length=254)
    toiletteur = forms.ModelChoiceField(queryset=Employee.objects.all(), initial=0)
    chien = forms.ModelMultipleChoiceField(queryset=Chien.objects.all(), initial=0)
    profession = forms.CharField(max_length=254)
    comment = forms.CharField(max_length=254)

    class Meta:
        fields = ('prenom', 'nom', 'adresse', 'num', 'toiletteur', 'chien', 'profession', 'comment')
        model = Client

class NewDog(forms.ModelForm):
    nom = forms.CharField(max_length=254)
    age = forms.CharField(max_length=254)
    race = forms.ModelChoiceField(queryset=Race.objects.all(), initial=0)
    comment = forms.CharField(max_length=255)

    class Meta:
        fields = ('nom', 'age', 'race')
        model = Chien

class NewRace(forms.ModelForm):
    race = forms.CharField(max_length=254)

    class Meta:
        fields = ('race',)
        model = Race