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

class Service(models.Model):
    RACE_CHOICE = (
    ("Petite", "Petit"),
    ("Moyenne", "Moyen"),
    ("Grande", "Grand"),
    )
    EXEC_CHOICE = (
        ("~ 5 min.", "5"),
        ("~ 30 min.", "30"),
        ("~ 1h00", "60"),
        ("~ 1h30", "90"),
        ("~ 2h00", "120"),
        ("~ 2h +", "+120")
    )

    service = models.CharField(max_length=255, null=True, default="")
    prix = models.DecimalField(max_digits=6, decimal_places=2, default="", null=True)
    race = models.CharField(max_length=9, choices=RACE_CHOICE, default="Moyenne")
    duree = models.CharField(max_length=9, choices=EXEC_CHOICE, default="~ 30 min.")

    def __str__(self):
        return self.service

class RDV(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, default="", null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, default="", null=True)
    date = models.DateTimeField()
    completed = models.DateTimeField(null=True)
    comment = models.TextField(max_length=255, default="", null=True)

    def __str__(self):
        return self.client.nom
