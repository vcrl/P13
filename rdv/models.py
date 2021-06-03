from os import truncate
from django.db import models
from datetime import date
from clients.models import Client
from services.models import Service
from employes.models import Employee
from django.utils import tree

class RDV(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, default="", null=True)
    service = models.ManyToManyField(Service, default="", null=True)
    date = models.DateTimeField(null=True)
    completed = models.DateTimeField(null=True)
    comment = models.TextField(max_length=255, default="", null=True)
    toiletteur = models.ForeignKey(Employee, on_delete=models.SET_NULL, default="", null=True)

    def __str__(self):
        return self.client.nom
