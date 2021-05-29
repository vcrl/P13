from os import truncate
from django.db import models
from datetime import date
from employes.models import Employee
from django.utils import tree

class Race(models.Model):
    race = models.CharField(max_length=155, default="", null=True)

    def __str__(self):
        return self.race

class Chien(models.Model):
    nom = models.CharField(max_length=155, default="", null=True)
    age = models.CharField(max_length=155, default="", null=True)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, default="", null=True)
    comment = models.CharField(max_length=255, default="", null=True)

    def __str__(self):
        return self.nom

class Client(models.Model):
    prenom = models.CharField(max_length=155, null=True)
    nom = models.CharField(max_length=155, default="", null=True)
    adresse = models.CharField(max_length=155, default="", null=True)
    num = models.CharField(max_length=255, default="", null=True)
    toiletteur = models.ForeignKey(Employee, on_delete=models.SET_NULL, default="", null=True)
    mail = models.CharField(max_length=255, default="", null=True)
    profession = models.CharField(max_length=155, null=True)
    comment = models.CharField(max_length=155, null=True)
    chien = models.ManyToManyField(Chien, default="", null=True)

    def __str__(self):
        return self.nom