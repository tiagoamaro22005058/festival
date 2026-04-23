from django.shortcuts import render
from .models import Palco, Dia, Concerto


def index_view(request):
    return render(request, 'festival/index.html')


def dias_view(request):
    dias = Dia.objects.all() 

    context = {'dias': dias}

    return render(request, 'festival/dias.html', context)



def concerto_view(request, id):
     concerto = Concerto.objects.get(id=id)

    context = {'concerto': concerto}

    return render(request, 'festival/concerto.html', context)

def palco_view(request):
    palco=Palco.objects.all()

    context= {'palcos': palco}

    return render(request, 'festival/palcos.html', context)
    
