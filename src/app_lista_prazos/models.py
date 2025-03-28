from django.db import models


# Create your models here.
class Prazo(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    prazo = models.PositiveSmallIntegerField(default=0)
