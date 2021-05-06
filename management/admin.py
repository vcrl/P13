from django.contrib import admin
from .models import Client, Chien, Race

# Register your models here.
admin.site.register(Chien)
admin.site.register(Client)
admin.site.register(Race)
