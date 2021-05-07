from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelChoiceField
from django.contrib.auth.models import User
from .models import Client, Chien, Race, Service, RDV
import datetime

class NewClient(forms.ModelForm):
    prenom = forms.CharField(max_length=254)
    nom = forms.CharField(max_length=254)
    adresse = forms.CharField(max_length=254)
    num = forms.CharField(max_length=254)
    toiletteur = forms.CharField(max_length=254)
    chien = forms.ModelChoiceField(queryset=Chien.objects.all(), initial=0)
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

class NewRDV(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), initial=0)
    service = forms.ModelMultipleChoiceField(queryset=Service.objects.all(), initial=0, widget=forms.CheckboxSelectMultiple)
    date = forms.DateField(initial=datetime.date.today)
    
    class Meta:
        fields = ('client', 'service', 'date')
        model = RDV

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