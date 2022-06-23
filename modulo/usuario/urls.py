from django.urls import path
from modulo.usuario.api import paciente_api_view


urlpatterns = [
    path('paciente/', paciente_api_view, name='Paciente_api' )
]
