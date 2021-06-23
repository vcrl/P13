from django.shortcuts import render, redirect, get_object_or_404
from .models import Service
from .forms import NewService
from django.utils import timezone
import datetime
from django.core.paginator import Paginator

# Manage super_context
def manage_super_context(super_context):
	if super_context["redirect"] is not None:
		return redirect(super_context["redirect"])
	if super_context["render"] is not None:
		return render(super_context["request"], super_context["render"], super_context["context"])

# EMPLOYEES GET CONTEXT
def services_context(request):
    super_context = init_super_context(request)
    services = get_service_by_service(request)
    super_context["render"] = "services/services.html"
    super_context["context"] = {'services':services}
    return super_context

# GET PARAMETERS
def get_service_by_service(request):
    return Service.objects.all().order_by("service")

# Init super_context
def init_super_context(request = None):
	return {
		"request": request,
		"redirect": None,
		"render": None,
		"context": None
	}