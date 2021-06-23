from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime
from rdv.models import RDV
from django.core.paginator import Paginator

@login_required
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

    return render(request, 'revenus/revenus_mensuel.html', {"month":current_month, "today":today, "rdv_list":rdv_list, 
    "gain_total":gain_total, "gain_tva":gain_tva, "gain_net":gain_net})

@login_required
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

    return render(request, 'revenus/revenus_annuels.html', {"month":current_month, "today":today, "rdv_list":rdv_list, 
    "gain_total":gain_total, "gain_tva":gain_tva, "gain_net":gain_net})