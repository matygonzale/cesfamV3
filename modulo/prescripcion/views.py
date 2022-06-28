from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'medico/index.html')



def get_prescripcion(request):
    prescripciones = list(Prescripcion.objects.all())
  
    datos = {'message': "Success", 'prescripciones': prescripciones}
    
    return JsonResponse(datos)