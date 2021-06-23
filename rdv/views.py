from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import RDV
from .forms import NewRDV
from django.utils import timezone
import datetime
from django.core.paginator import Paginator

@login_required
def add_rdv(request):
    form = NewRDV
    return render(request, "rdv/add_rdv.html", {'form':form})

@login_required
def save_rdv(request):
    if request.method == "POST":
        form = NewRDV(request.POST)
        if form.is_valid():
            form.save()
    return redirect("rdv_list")  

@login_required
def rdv_details(request, rdv_pk):
    rdv = get_object_or_404(RDV, pk=rdv_pk)
    return render(request, "rdv/rdv_detail.html", {"rdv":rdv})

@login_required
def rdv_list(request):
    rdvs = RDV.objects.all().order_by("date")
    return render(request, "rdv/rdv_list.html", {"rdvs":rdvs})

@login_required
def rdv_complete(request, rdv_pk):
    rdv = get_object_or_404(RDV, pk=rdv_pk)
    if request.method == "POST":
        rdv.completed = timezone.now()
        rdv.save()
        return redirect("rdv_list")
    else:
        return redirect("rdv_list")

@login_required
def rdv_delete(request, rdv_pk):
    if request.method == "POST":
        rdv = get_object_or_404(RDV, pk=rdv_pk)
        rdv.delete()
        return redirect("rdv_list")
    else:
        return redirect("rdv_list")