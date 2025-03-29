from datetime import datetime, timedelta
from django.db import models


# Create your models here.
class Prazo(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    prazo = models.PositiveSmallIntegerField(default=0)

    def get_data_vencimento(self):
        return datetime.now() + timedelta(days=self.prazo)

    def __str__(self):
        return f"{self.id} - {self.prazo} dias | Vence em {self.get_data_vencimento().strftime(f'%d/%m/%Y')}"
