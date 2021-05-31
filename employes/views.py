from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import NewEmployee
from django.utils import timezone
import datetime
from django.core.paginator import Paginator

# Employés.
def add_employee(request):
    form = NewEmployee()
    return render(request, "employes/add_employee.html", {'form':form})

def employees(request):
    employees = Employee.objects.all().order_by('nom')
    chiens = Employee.objects.all()

    clients_paginator = Paginator(employees, 6)
    page_number = request.GET.get("page")
    page = clients_paginator.get_page(page_number)
    return render(request, "employes/employees.html", {'employee':employees, 'chiens':chiens, 'page':page, 'count':clients_paginator.count})

def save_employee(request):
    if request.method == "POST":
        form = NewEmployee(request.POST)
        if form.is_valid():
            form.save()
        return redirect("employees")

def employee_delete(request, employee_pk):
    if request.method == "POST":
        client = get_object_or_404(Employee, pk=employee_pk)
        client.delete()
        return redirect("employees")
    else:
        return redirect("employees")

def employee_edit(request, employee_pk):
    employee = get_object_or_404(Employee, pk=employee_pk)
    form = NewEmployee(request.POST or None, instance=employee)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("employees")
        else:
            return redirect("employees")
    return render(request, "employes/edit_employee.html", {'employee':employee, 'form':form})