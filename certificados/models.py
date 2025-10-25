from django.db import models
from cadastro.models import Matricula, Turma

# Create your models here.
class Certificado(models.Model):
    matricula_id = models.ForeignKey(Matricula, null=False, blank=False, on_delete=models.RESTRICT)
    turma_id = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.RESTRICT)
    path_certificado = models.TextField(null=True, blank=True)