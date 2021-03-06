from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Service
from .forms import NewService
from django.utils import timezone
import datetime
from django.core.paginator import Paginator

@login_required
def services(request):
    services = Service.objects.all().order_by("service")
    return render(request, "services/services.html", {'services':services})

@login_required
def add_service(request):
    form = NewService()
    return render(request, "services/add_service.html", {'form':form})

@login_required
def save_service(request):
    if request.method == "POST":
        form = NewService(request.POST)
        if form.is_valid():
            form.save()
        return redirect("services")
    else:
        return redirect("services")

@login_required
def service_details(request, service_pk):
    service = get_object_or_404(Service, pk=service_pk)
    return render(request, 'services/service_detail.html', {'service':service})

@login_required
def service_delete(request, service_pk):
    if request.method == "POST":
        service = get_object_or_404(Service, pk=service_pk)
        service.delete()
        return redirect("services")
    else:
        return redirect("services")