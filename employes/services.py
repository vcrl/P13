from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import NewEmployee
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
def get_employees_context(request):
    super_context = init_super_context(request)
    employees = get_employees(by_name=True)
    chiens = get_employees()

    clients_paginator = Paginator(employees, 6)
    page_number = request.GET.get("page")
    page = clients_paginator.get_page(page_number)
    super_context["render"] = "employes/employees.html"
    super_context["context"] = {'employee':employees, 'chiens':chiens, 'page':page, 'count':clients_paginator.count}
    return super_context

def save_employee_context(request):
    super_context = init_super_context(request)
    if request.method == "POST":
        form = get_new_employee_form(request)
        if form.is_valid():
            form.save()
        super_context["redirect"] = "employees"
        return super_context

def employee_delete_context(request, employee_pk):
    super_context = init_super_context(request)
    if request.method == "POST":
        client = get_employee_or_404(employee_pk=employee_pk)
        client.delete()
        super_context["redirect"] = "employees"
        return super_context
    else:
        super_context["redirect"] = "employees"
        return super_context

def employee_edit_context(request, employee_pk):
    super_context = init_super_context(request)
    employee = get_employee_or_404(employee_pk)
    form = get_new_employee_form(request, instance=employee)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            super_context["redirect"] = "employees"
            return super_context
        else:
            super_context["redirect"] = "employees"
            return super_context
    super_context["render"] = "employes/edit_employee.html"
    super_context["context"] = {'employee':employee, 'form':form}
    return super_context

# GET PARAMETERS
def get_employee_or_404(employee_pk):
    return get_object_or_404(Employee, pk=employee_pk)

def get_new_employee_form(request=None, instance=None):
    if request:
        return NewEmployee(request.POST or None, instance=instance)
    else:
        return NewEmployee()

def get_employees(by_name=False):
    if by_name:
        return Employee.objects.all().order_by('nom')
    else:
        return Employee.objects.all()

# Init super_context
def init_super_context(request = None):
	return {
		"request": request,
		"redirect": None,
		"render": None,
		"context": None
	}