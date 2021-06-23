from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Chien
from .forms import NewClient, NewDog, NewRace
from django.utils import timezone
import datetime
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .services import add_client_context, add_dog_context, add_race_context, get_client_delete_context, get_clients_context, get_dogs_context, manage_super_context, get_client_edit_context, save_client_context, save_dog_context, save_race_context

# Clients.
@login_required
def add_client(request):
    return manage_super_context(add_client_context(request))

@login_required
def clients(request):
    return manage_super_context(get_clients_context(request))

@login_required
def save_client(request):
    return manage_super_context(save_client_context(request))

@login_required
def client_delete(request, client_pk):
    return manage_super_context(get_client_delete_context(request, client_pk))

@login_required
def client_edit(request, client_pk):
    return manage_super_context(get_client_edit_context(request, client_pk))

# Chiens.
@login_required
def add_dog(request):
    return manage_super_context(add_dog_context(request))

@login_required
def dogs(request):
    return manage_super_context(get_dogs_context(request))

@login_required
def save_dog(request):
    return manage_super_context(save_dog_context(request))

# Races.
@login_required
def add_race(request):
    return manage_super_context(add_race_context(request))

@login_required
def save_race(request):
    return manage_super_context(save_race_context(request))