from django.shortcuts import render
from management.models import *

# Create your views here.
def frontpage(request):
    clients = Client.objects.all().count()
    chiens = Chien.objects.all().count()
    races = Race.objects.all().count()
    return render(request, "frontpage/index.html", {'chiens':chiens, 'clients':clients, 'races':races})