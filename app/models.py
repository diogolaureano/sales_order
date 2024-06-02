from django.db import models

# Create your models here.

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    data_da_venda = models.DateField()
    cliente = models.CharField(max_length=255)
    produto = models.TextField(max_length=255)
    quantidade = models.DecimalField(max_digits=10,decimal_places=2)
    valor_de_venda = models.DecimalField(max_digits=10,decimal_places=2)
    taxas = models.DecimalField(max_digits=10,decimal_places=2)
    valor_liquido = models.DecimalField(max_digits=10,decimal_places=2)
    prazo = models.DateField()
    canal_de_venda = models.CharField(max_length=255)
    codigo_de_rastreio = models.CharField(max_length=255)

class Movimentacao(models.Model):
    
    CATEGORY_CHOICES = [
        ('1', 'Receita'),
        ('2', 'Custo'),
        ('3', 'Descpesa')
    ]
      
    id_movimentacao = models.AutoField(primary_key=True)
    tipo_movimentacao = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='1')
    descricao_movimentacao = models.TextField(max_length=255)
    valor_movimentacao = models.DecimalField(max_digits=10,decimal_places=2)
    saldo_movimentacao = models.DecimalField(max_digits=10,decimal_places=2)    
    
    
    
    