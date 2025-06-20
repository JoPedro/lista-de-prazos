from datetime import datetime, timedelta
from django.db import models
from django.utils import timezone


# Create your models here.
class Prazo(models.Model):
    identificador = models.CharField(max_length=255, unique=True)
    data_de_início = models.DateTimeField(default=timezone.now)
    prazo_1_em_dias = models.PositiveSmallIntegerField(default=0)
    prazo_2_em_dias = models.PositiveSmallIntegerField(default=0)

    @property
    def data_de_vencimento_1(self):
        return self.data_de_início + timedelta(days=self.prazo_1_em_dias)

    @property
    def data_de_vencimento_2(self):
        return self.data_de_início + timedelta(days=self.prazo_2_em_dias)

    @property
    def dias_para_vencer_1(self):
        return (self.data_de_vencimento_1 - timezone.now()).days + 1

    @property
    def dias_para_vencer_2(self):
        return (self.data_de_vencimento_2 - timezone.now()).days + 1

    def __str__(self):
        return f"{self.identificador} - {self.prazo_1_em_dias} dias/{self.prazo_2_em_dias} dias | Vence em {self.data_de_vencimento_1.strftime(f'%d/%m/%Y')} ({self.dias_para_vencer_1} dias)/{self.data_de_vencimento_2.strftime(f'%d/%m/%Y')} ({self.dias_para_vencer_2} dias)"
