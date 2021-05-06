from django.shortcuts import render, redirect
from .models import Client, Chien, Race, Service, RDV
from .forms import NewClient, NewDog, NewRace, NewRDV

# Clients.
def add_client(request):
    form = NewClient()
    return render(request, "management/add_client.html", {'form':form})

def clients(request):
    clients = Client.objects.all().order_by('nom')
    chiens = Chien.objects.all()
    return render(request, "management/clients.html", {'clients':clients, 'chiens':chiens})

def save_client(request):
    if request.method == "POST":
        form = NewClient(request.POST)
        if form.is_valid():
            form.save()
        return redirect("clients")

# Chiens.
def add_dog(request):
    form = NewDog()
    return render(request, "management/add_dog.html", {'form':form})

def dogs(request):
    clients = Client.objects.all()
    chiens = Chien.objects.all().order_by('nom')
    return render(request, "management/dogs.html", {'clients':clients, 'chiens':chiens})

def save_dog(request):
    if request.method == "POST":
        form = NewDog(request.POST)
        if form.is_valid():
            form.save()
        return redirect("dogs")

# Races.
def add_race(request):
    form = NewRace()
    return render(request, "management/add_race.html", {'form':form})

def save_race(request):
    if request.method == "POST":
        form = NewRace(request.POST)
        if form.is_valid():
            form.save()
        return redirect("add_race")

def calendar(request):
    return render(request, "management/calendar.html")

# Services.
def services(request):
    services = Service.objects.all().order_by("service")
    return render(request, "management/services.html", {'services':services})

# RDV.
def add_rdv(request):
    form = NewRDV
    return render(request, "management/add_rdv.html", {'form':form})