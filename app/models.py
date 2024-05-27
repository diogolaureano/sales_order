from django.db import models

# Create your models here.

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    data_da_venda = models.IntegerField(None)
    cliente = models.TextField(max_length=255)
    produto = models.TextField(max_length=255)
    quantidade = models.TextField(max_length=255)
    valor_de_venda = models.TextField(max_length=255)
    taxas = models.TextField(max_length=255)
    valor_liquido = models.TextField(max_length=255)
    prazo = models.TextField(max_length=255)
    canal_de_venda = models.TextField(max_length=255)
    codigo_de_rastreio = models.TextField(max_length=255)