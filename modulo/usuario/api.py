from cProfile import run
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from modulo.usuario.serializers import *
from modulo.usuario.models import *

@api_view(['GET','POST'])
def paciente_api_view(request):
    
    if request.method == 'GET':
        usuarios = Paciente.objects.all()
        usuarios_serializador = PacienteSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = PacienteSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
@api_view(['GET','PUT','DELETE'])
def paciente_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = Paciente.objects.filter(Run = pk).first()
        usuarios_serializador = PacienteSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = Paciente.objects.filter(Run = pk).first()
        usuarios_serializador = PacienteSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors) 
    
    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = Paciente.objects.filter(Run = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Error')
    