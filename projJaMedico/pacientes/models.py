from django.db import models

class Paciente(models.Model):
    nome_completo = models.CharField(max_length=30)
    cpf_paciente = models.CharField(max_length=30)