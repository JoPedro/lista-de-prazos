from datetime import datetime, timedelta
from django.db import models


# Create your models here.
class Prazo(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    prazo_em_dias = models.PositiveSmallIntegerField(default=0)

    @property
    def data_vencimento(self):
        return datetime.today() + timedelta(days=self.prazo_em_dias)

    @property
    def dias_para_vencer(self):
        return (self.data_vencimento - datetime.today()).days

    def __str__(self):
        return f"{self.id} - {self.prazo_em_dias} dias | Vence em {self.data_vencimento.strftime(f'%d/%m/%Y')} ({self.dias_para_vencer} dias)"
