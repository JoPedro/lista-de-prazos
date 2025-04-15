from datetime import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Prazo(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    prazo_em_dias = models.PositiveSmallIntegerField(default=0)
    data_de_vencimento = models.DateTimeField(default=timezone.now)

    @property
    def dias_para_vencer(self):
        return (self.data_de_vencimento - timezone.now()).days + 1

    def __str__(self):
        return f"{self.id} - {self.prazo_em_dias} dias | Vence em {self.data_de_vencimento.strftime(f'%d/%m/%Y')} ({self.dias_para_vencer} dias)"
