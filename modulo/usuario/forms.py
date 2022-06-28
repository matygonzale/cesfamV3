from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        
class Paciente_EditarForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ["Run", "dv", "nombre", "apellido", "telefono", "cronico",
                  "tutor", "telefono_tutor", "nacimiento", "direccion", "genero"]