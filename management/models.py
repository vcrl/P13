from django.db import models

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
    toiletteur = models.CharField(max_length=255, default="", null=True)
    mail = models.CharField(max_length=255, default="", null=True)
    profession = models.CharField(max_length=155, null=True)
    comment = models.CharField(max_length=155, null=True)
    chien = models.ForeignKey(Chien, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nom