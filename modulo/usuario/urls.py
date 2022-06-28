from unicodedata import name
from django.urls import path
from modulo.usuario.api import *
from modulo.usuario.views import *


urlpatterns = [
    path('paciente/', paciente_api_view, name='paciente_api' ),
    path('paciente/<int:pk>/', paciente_detail_view, name='paciente_detial_api'),
    path('index/', index, name= 'index'),
    path('crearpaciente/', crear_paciente, name= 'crearpaciente'),
    path('editarpaciente/<int:pk>/', editar_paciente, name= 'editarpaciente')
]
