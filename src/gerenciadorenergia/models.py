from django.db import models

# Create your models here.

class InfoConsumo(models.Model):
    nome_dispositivo = models.TextField(max_length=255)
    consumo = models.FloatField()
    corrente = models.FloatField()
