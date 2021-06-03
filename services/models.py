from os import truncate
from django.db import models
from datetime import date
from django.utils import tree

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
    race = models.CharField(max_length=9, choices=RACE_CHOICE, default="Moyenne", null=True)
    duree = models.CharField(max_length=9, choices=EXEC_CHOICE, default="~ 30 min.", null=True)

    def __str__(self):
        return self.service
