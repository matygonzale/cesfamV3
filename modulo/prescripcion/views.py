from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'medico/index.html')



def get_prescripcion(self, request):
    prescripciones = list(Prescripcion.objects.values())
    if len(Prescripcion) > 0:
        datos = {'message': "Success", 'prescripciones': prescripciones}
    else:
        datos = {'message': "Prescripciones not found..."} 
    return JsonResponse(datos)