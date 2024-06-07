from django.db import models

# Create your models here.

# class Pedido(models.Model):
#     id_pedido = models.AutoField(primary_key=True)
#     data_da_venda = models.DateField()
#     cliente = models.TextField(max_length=255)
#     produto = models.TextField(max_length=255)
#     quantidade = models.IntegerField(max_length=255)
#     valor_de_venda = models.IntegerField(max_length=255)
#     taxas = models.IntegerField(max_length=255)
#     valor_liquido = models.IntegerField(max_length=255)
#     prazo = models.DateField()
#     canal_de_venda = models.TextField(max_length=255)
#     codigo_de_rastreio = models.TextField(max_length=255)

class Pedido(models.Model):
    numero_pedido = models.AutoField(primary_key=True)
    data_emissao = models.DateField()
    cliente = models.CharField(max_length=100)
    produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    valor_bruto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    taxas = models.DecimalField(max_digits=10, decimal_places=2)
    valor_liquido = models.DecimalField(max_digits=10, decimal_places=2)
    observacoes = models.TextField(blank=True, null=True)
    prazo_entrega = models.DateField()

    def _str_(self):
        return f"Pedido {self.numero_pedido} - {self.cliente}"

class Produto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=255)

    def _str_(self):
        return self.descricao
    
class Cliente(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    celular = models.CharField(max_length=20)

    def _str_(self):
        return self.nome
    
class Movimentacao(models.Model):
    TIPO_CHOICES = (
        ('C', 'Custo'),
        ('D', 'Despesa'),
        ('R', 'Receita'),
    )
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    descricao = models.CharField(max_length=255)

    def _str_(self):
        return self.descricao
    
class Financeiro(models.Model):
    TIPO_CHOICES = (
        ('C', 'Crédito'),
        ('D', 'Débito'),
    )
    data = models.DateField()
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    descricao = models.CharField(max_length=255)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return self.descricao
    
