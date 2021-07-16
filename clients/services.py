from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Chien
from .forms import NewClient, NewDog, NewRace
from django.core.paginator import Paginator

# Manage super_context
def manage_super_context(super_context):
	if super_context["redirect"] is not None:
		return redirect(super_context["redirect"])
	if super_context["render"] is not None:
		return render(super_context["request"], super_context["render"], super_context["context"])

# CLIENTS GET CONTEXT
def get_client_edit_context(request, client_pk):
	super_context = init_super_context(request)

	client = get_client(client_pk)
	form = get_form(request, client)

	super_context["context"] = {'client':client, 'form':form}

	if request.method == "POST":
		if form.is_valid():
			form.save()
			super_context["redirect"] = "clients"
	super_context["render"] = "clients/edit_client.html"
	return super_context

def get_client_delete_context(request, client_pk):
	super_context = init_super_context(request)
	if request.method == "POST":
		client = get_client(client_pk)
		client.delete()
		super_context["redirect"] = "clients"
	return super_context

def get_clients_context(request):
	super_context = init_super_context(request)
	clients = get_clients(by_name=True)
	chiens = get_dogs()

	clients_paginator = Paginator(clients, 6)
	page_number = request.GET.get("page")
	page = clients_paginator.get_page(page_number)

	super_context["context"] = {'clients':clients, 'chiens':chiens, 'page':page, 'count':clients_paginator.count}
	super_context["render"] = "clients/clients.html"
	return super_context

def save_client_context(request):
	super_context = init_super_context(request)
	if request.method == "POST":
		form = NewClient(request.POST)#get_new_client_form(request)
		if form.is_valid():
			form.save()
		else:
			for i in range(100):
				print("non")
		super_context["redirect"] = "clients"
		return super_context

def add_client_context(request):
	super_context = init_super_context(request)
	form = get_new_client_form(request)
	super_context["render"] = "clients/add_client.html"
	super_context["context"] = {'form':form}
	return super_context

# DOGS GET CONTEXT
def add_dog_context(request):
	super_context = init_super_context(request)
	form = get_new_dog_form()
	super_context["render"] = "clients/add_dog.html"
	super_context["context"] = {'form':form}
	return super_context

def get_dogs_context(request):
	super_context = init_super_context(request)
	clients = get_clients(by_name=False)
	chiens = get_dogs(by_name=True)
	chiens_paginator = Paginator(chiens, 6)
	page_number = request.GET.get("page")
	page = chiens_paginator.get_page(page_number)
	super_context["render"] = "clients/dogs.html"
	super_context["context"] = {'clients':clients, 'chiens':chiens, 'page':page}
	return super_context

def save_dog_context(request):
	super_context = init_super_context(request)
	if request.method == "POST":
		form = get_new_dog_form(request)
		if form.is_valid():
			form.save()
		super_context["redirect"] = "dogs"
		return super_context

# RACE GET CONTEXT
def add_race_context(request):
	super_context = init_super_context(request)
	form = get_new_race_form()
	super_context["render"] = "clients/add_race.html"
	super_context["context"] = {'form':form}
	return super_context

def save_race_context(request):
	super_context = init_super_context(request)
	if request.method == "POST":
		form = get_new_race_form(request)
		if form.is_valid():
			form.save()
		super_context["redirect"] = "add_race"
	return super_context

# GET PARAMETERS
def get_new_race_form(request=None):
	if request:
		return NewRace(request.POST)
	else:
		return NewRace()

def get_dogs(by_name = False):
	if by_name:
		return Chien.objects.all().order_by('nom')
	else:
		return Chien.objects.all()

def get_new_dog_form(request=None):
	if request:
		return NewDog(request.POST)
	else:
		return NewDog()

def get_new_client_form_post(request):
	return NewClient(request.POST)

def get_new_client_form(request):
	return NewClient()

def get_client(client_pk):
	return get_object_or_404(Client, pk=client_pk)

def get_clients(by_name = False):
	if by_name:
		return Client.objects.all().order_by('nom')
	else:
		return Client.objects.all()

def get_form(request, client):
	return NewClient(request.POST or None, instance=client)

# Init super_context
def init_super_context(request = None):
	return {
		"request": request,
		"redirect": None,
		"render": None,
		"context": None
	}