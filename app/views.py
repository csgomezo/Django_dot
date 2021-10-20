from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from app.models import socio, prestamo
from rest_framework.decorators import api_view
import psycopg2
from config import Config
from django.db.models import Avg, Max, Min
from django import forms

# Create your views here.
def index(request):
    template = loader.get_template('base/base.html')
    return HttpResponse(template.render())

class Home(generic.TemplateView):
    template_name="base/base.html"

def valorF(request):
    valorActual = int(request.POST['monto'])
    n = 36
    pk = int(request.POST['pk'])
    socioEl = socio.objects.get(id = pk)
    i = socioEl.tasa
    valorFinal = round(valorActual * (1+(i/100)*n),2)
    valorMensual = round(valorFinal/n,2)
    return render(request, 'base/base.html',{'VF':valorFinal, 'socio':socioEl,'tasa':i,'ValorM':valorMensual, 'montoP':valorActual,'pk':pk})

@api_view(['GET', 'POST', 'DELETE'])
def showSoc(request):
    monto = int(request.POST['monto'])
    fallo = False
    ret =''
    socios = socio.objects.filter(montoDisponible__gt = monto-1).order_by('tasa')
    listaSocios = []
    minimo = 5
    for x in socios:
        temp = x.tasa
        if minimo >= temp:
            minimo = temp
            listaSocios.append(x)
        else:
            pass
    try:
        socios2 = listaSocios
    except:
        ret = "No hay socio disponible"
        fallo = True
    return render(request, 'base/base.html', {'soc':socios2, 'fallo':fallo, 'ret':ret, 'monto':monto})

def aceptarPrestamo(request):
    monto = int(request.POST['montoP'])
    pk = int(request.POST['pkP'])
    socioPrestamo = socio.objects.get(id = pk)
    socioMontoAnt = socioPrestamo.montoDisponible
    socioMontoNuevo = socioMontoAnt - monto
    socioPrestamo.montoDisponible = socioMontoNuevo
    fallo = False
    acept = False
    try:
        socioPrestamo.save()
        acep = True
    except e:
        fall = True
    #,[socioPres[0].id]
    return render(request, 'base/base.html', {'acep':acep,})