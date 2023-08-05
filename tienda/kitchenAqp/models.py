from django.db import models
from .choises import Tipo
class comidas(models.Model):
    id = int
    name = models.CharField(max_length=100)
    tipo = models.CharField(max_length=2, choices=Tipo, default='4')
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(default='')
    price = models.IntegerField()
