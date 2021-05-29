from os import truncate
from django.db import models
from datetime import date

from django.utils import tree

class Employee(models.Model):
    prenom = models.CharField(max_length=155, null=True)
    nom = models.CharField(max_length=155, default="", null=True)
    adresse = models.CharField(max_length=155, default="", null=True)
    num = models.CharField(max_length=255, default="", null=True)
    rdv_number = models.IntegerField(default=0, null=True)
    joined = models.DateTimeField(null=True)
    fired = models.DateTimeField(null=True)

    def __str__(self):
        return self.nom