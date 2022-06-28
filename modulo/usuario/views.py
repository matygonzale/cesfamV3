from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.

def index(request):
    personas = Paciente.objects.all()
    contexto = {
        'form' : personas
    }
    return render(request, 'medico/prueba.html', contexto)
 
def crear_paciente(request):
    
    if request.method == 'GET':
        
        paciente = PacienteForm()
        contexto = {
            'form' : paciente
        }

    else:
        paciente = PacienteForm(request.POST)
                
        contexto = {
            'form' : paciente
        }
        if paciente.is_valid():
            paciente.save()
            
    return render(request, 'medico/crearpaciente.html', contexto)

def editar_paciente(request, pk):
    persona = Paciente.objects.get(Run = pk)
    
    if request.method == 'GET':
        
        paciente = PacienteForm(instance = persona)
        contexto = {
            'form' : paciente
        }
    elif request.method == 'POST':
        
        mi_run = request.POST['Run']
        mi_dv = request.POST['dv']
        mi_nombre = request.POST['nombre']
        mi_apellido = request.POST['apellido']
        mi_telefono = request.POST['telefono']
        mi_tutor = request.POST['tutor']
        mi_telefono_tutor = request.POST['telefono_tutor']
        mi_nacimiento = request.POST['nacimiento']
        mi_direccion = request.POST['direccion']
        mi_genero = request.POST['genero']
        mi_correo = request.POST['correo']
        mi_idCarnet = request.POST['idCarnet_Paciente']
        if mi_run != "":
            personaa = PacienteForm(instance = persona)
            personaa.Run = mi_run
            personaa.dv = mi_dv
            personaa.nombre = mi_nombre
            personaa.apellido = mi_apellido
            personaa.telefono = mi_telefono
            personaa.tutor = mi_tutor
            personaa.telefono_tutor = mi_telefono_tutor
            personaa.nacimiento = mi_nacimiento
            personaa.direccion = mi_direccion
            personaa.genero = mi_genero
            personaa.correo = mi_correo
            personaa.idcarnet_Paciente = mi_idCarnet
            
            contexto = {
            'form' : personaa
            }
            if personaa.is_valid():
                print (personaa)
                personaa.save()
            
            
            
            
    return render(request, 'medico/prueba.html', contexto)

def actualizar_paciente(request):
    
    return