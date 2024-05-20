from django.db import models

# Create your models here.

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    pedido = models.IntegerField()
    cliente = models.TextField(max_length=255)