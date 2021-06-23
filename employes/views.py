from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import NewEmployee
from django.utils import timezone
import datetime
from django.core.paginator import Paginator
from .services import employee_delete_context, employee_edit_context, get_employees_context, manage_super_context, save_employee_context

# Employés.
@login_required
def add_employee(request):
    form = NewEmployee()
    return render(request, "employes/add_employee.html", {'form':form})

@login_required
def employees(request):
    return manage_super_context(get_employees_context(request))

@login_required
def save_employee(request):
    return manage_super_context(save_employee_context(request))

@login_required
def employee_delete(request, employee_pk):
    return manage_super_context(employee_delete_context(request, employee_pk))

@login_required
def employee_edit(request, employee_pk):
    return manage_super_context(employee_edit_context(request, employee_pk))