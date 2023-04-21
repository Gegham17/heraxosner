from django.shortcuts import render
from .models import Heraxos
# Create your views here.

def home(request):
    heraxos_list = Heraxos.objects.all()
    return render(request, 'home.html', context={
        'heraxos_list':heraxos_list
    })