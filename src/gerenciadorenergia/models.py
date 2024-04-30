from django.utils import timezone
from typing import Iterable
from django.db import models

# Create your models here.

class InfoConsumo(models.Model):
    nome_dispositivo = models.TextField(max_length=255)
    consumo = models.FloatField()
    corrente = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)

    def save(self):
        self.date_time = self.date_time.astimezone(timezone.get_current_timezone())
        return super().save(self)

    def __str__(self):
        return '{} {}'.format(self.nome_dispositivo, self.pk)
