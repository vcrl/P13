from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Chien, Race, Service, RDV, Employee
from .forms import NewClient, NewDog, NewRace, NewRDV, NewService, NewEmployee
from django.utils import timezone
import datetime
from django.core.paginator import Paginator

# Clients.
def add_client(request):
    form = NewClient()
    return render(request, "management/add_client.html", {'form':form})

def clients(request):
    clients = Client.objects.all().order_by('nom')
    chiens = Chien.objects.all()

    clients_paginator = Paginator(clients, 6)
    page_number = request.GET.get("page")
    page = clients_paginator.get_page(page_number)
    return render(request, "management/clients.html", {'clients':clients, 'chiens':chiens, 'page':page, 'count':clients_paginator.count})

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

# Chiens.
def add_dog(request):
    form = NewDog()
    return render(request, "management/add_dog.html", {'form':form})

def dogs(request):
    clients = Client.objects.all()
    chiens = Chien.objects.all().order_by('nom')
    chiens_paginator = Paginator(chiens, 6)
    page_number = request.GET.get("page")
    page = chiens_paginator.get_page(page_number)
    return render(request, "management/dogs.html", {'clients':clients, 'chiens':chiens, 'page':page})

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

def add_service(request):
    form = NewService()
    return render(request, "management/add_service.html", {'form':form})

def save_service(request):
    if request.method == "POST":
        form = NewService(request.POST)
        if form.is_valid():
            form.save()
        return redirect("services")

def service_details(request, service_pk):
    service = get_object_or_404(Service, pk=service_pk)
    return render(request, 'management/service_detail.html', {'service':service})

def service_delete(request, service_pk):
    if request.method == "POST":
        service = get_object_or_404(Service, pk=service_pk)
        service.delete()
        return redirect("services")

# RDV.
def add_rdv(request):
    form = NewRDV
    return render(request, "management/add_rdv.html", {'form':form})

def save_rdv(request):
    if request.method == "POST":
        form = NewRDV(request.POST)
        if form.is_valid():
            form.save()
    return redirect("rdv_list")  

def rdv_details(request, rdv_pk):
    rdv = get_object_or_404(RDV, pk=rdv_pk)
    return render(request, "management/rdv_detail.html", {"rdv":rdv})

def rdv_list(request):
    rdvs = RDV.objects.all().order_by("date")
    return render(request, "management/rdv_list.html", {"rdvs":rdvs})

def rdv_complete(request, rdv_pk):
    rdv = get_object_or_404(RDV, pk=rdv_pk)
    if request.method == "POST":
        rdv.completed = timezone.now()
        rdv.save()
        return redirect("rdv_list")

def rdv_delete(request, rdv_pk):
    if request.method == "POST":
        rdv = get_object_or_404(RDV, pk=rdv_pk)
        rdv.delete()
        return redirect("rdv_list")

# Revenus.
def revenus_mensuel(request):
    today = datetime.date.today()
    months = ['zero','Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
    current_month = months[today.month]

    rdvs = RDV.objects.all()
    rdv_list = []
    gain_total = 0
    for rdv in rdvs:
        if rdv.completed:
            if rdv.completed.month == today.month:
                rdv_list.append(rdv)
    
    for rdv in rdv_list:
        for prix in rdv.service.all():
            gain_total += prix.prix

    gain_tva = float(gain_total) * 20 / 100

    gain_net = float(gain_total) - gain_tva

    return render(request, 'management/revenus_mensuel.html', {"month":current_month, "today":today, "rdv_list":rdv_list, 
    "gain_total":gain_total, "gain_tva":gain_tva, "gain_net":gain_net})

def revenus_annuels(request):
    today = datetime.date.today()
    months = ['zero','Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
    current_month = months[today.month]

    rdvs = RDV.objects.all()
    rdv_list = []
    gain_total = 0
    for rdv in rdvs:
        if rdv.completed:
            if rdv.completed.year == today.year:
                rdv_list.append(rdv)
    
    for rdv in rdv_list:
        for prix in rdv.service.all():
            gain_total += prix.prix

    gain_tva = float(gain_total) * 20 / 100

    gain_net = float(gain_total) - gain_tva

    return render(request, 'management/revenus_annuels.html', {"month":current_month, "today":today, "rdv_list":rdv_list, 
    "gain_total":gain_total, "gain_tva":gain_tva, "gain_net":gain_net})


# Employés.
def add_employee(request):
    form = NewEmployee()
    return render(request, "management/add_employee.html", {'form':form})

def employees(request):
    clients = Client.objects.all().order_by('nom')
    chiens = Chien.objects.all()

    clients_paginator = Paginator(clients, 6)
    page_number = request.GET.get("page")
    page = clients_paginator.get_page(page_number)
    return render(request, "management/clients.html", {'clients':clients, 'chiens':chiens, 'page':page, 'count':clients_paginator.count})

def save_employee(request):
    if request.method == "POST":
        form = NewClient(request.POST)
        if form.is_valid():
            form.save()
        return redirect("clients")

def employee_delete(request, client_pk):
    if request.method == "POST":
        client = get_object_or_404(Client, pk=client_pk)
        client.delete()
        return redirect("clients")