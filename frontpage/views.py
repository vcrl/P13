from django.shortcuts import render
from clients.models import Client, Chien, Race
from rdv.models import RDV
import datetime

# Create your views here.
def frontpage(request):
    clients = Client.objects.all().count()
    chiens = Chien.objects.all().count()
    races = Race.objects.all().count()
    rdv = RDV.objects.all().count()
    gain_net = calcule_monthly_income()
    return render(request, "frontpage/index.html", {'chiens':chiens, 'clients':clients, 'races':races, "rdv":rdv, "gain_net":gain_net})

def calcule_monthly_income():
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

    return gain_net