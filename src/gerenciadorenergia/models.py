from django.db import models

# Create your models here.

class InfoConsumo(models.Model):
    nome_dispositivo = models.TextField(max_length=255)
    consumo = models.FloatField()
    corrente = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)
