from django.db import models


class Paciente(models.Model):
    nome_completo = models.CharField(max_length=30)
    cpf_paciente = models.CharField(max_length=30)
    foto_paciente = models.ImageField(upload_to='pacientes_fotos', null=True, blank=True)

    def __str__(self):
        return self.nome_completo
