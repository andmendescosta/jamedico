from django.forms import ModelForm
from .models import Paciente


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = {'nome_completo', 'cpf_paciente', 'foto_paciente'}
