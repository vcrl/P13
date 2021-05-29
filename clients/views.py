from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Chien
from .forms import NewClient, NewDog, NewRace
from django.utils import timezone
import datetime
from django.core.paginator import Paginator

# Clients.
def add_client(request):
    form = NewClient()
    return render(request, "clients/add_client.html", {'form':form})

def clients(request):
    clients = Client.objects.all().order_by('nom')
    chiens = Chien.objects.all()

    clients_paginator = Paginator(clients, 6)
    page_number = request.GET.get("page")
    page = clients_paginator.get_page(page_number)
    return render(request, "clients/clients.html", {'clients':clients, 'chiens':chiens, 'page':page, 'count':clients_paginator.count})

def save_client(request):
    if request.method == "POST":
        form = NewClient(request.POST)
        if form.is_valid():
            form.save()
        return redirect("clients")

def client_delete(request, client_pk):
    if request.method == "POST":
        client = get_object_or_404(Client, pk=client_pk)
        client.delete()
        return redirect("clients")

def client_edit(request, client_pk):
    client = get_object_or_404(Client, pk=client_pk)
    form = NewClient(request.POST or None, instance=client)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("clients")
    return render(request, "clients/edit_client.html", {'client':client, 'form':form})

# Chiens.
def add_dog(request):
    form = NewDog()
    return render(request, "clients/add_dog.html", {'form':form})

def dogs(request):
    clients = Client.objects.all()
    chiens = Chien.objects.all().order_by('nom')
    chiens_paginator = Paginator(chiens, 6)
    page_number = request.GET.get("page")
    page = chiens_paginator.get_page(page_number)
    return render(request, "clients/dogs.html", {'clients':clients, 'chiens':chiens, 'page':page})

def save_dog(request):
    if request.method == "POST":
        form = NewDog(request.POST)
        if form.is_valid():
            form.save()
        return redirect("dogs")

# Races.
def add_race(request):
    form = NewRace()
    return render(request, "clients/add_race.html", {'form':form})

def save_race(request):
    if request.method == "POST":
        form = NewRace(request.POST)
        if form.is_valid():
            form.save()
        return redirect("add_race")