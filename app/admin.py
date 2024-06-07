from django.contrib import admin
from .models import Pedido, Produto, Cliente, Movimentacao, Financeiro

# Register the models
admin.site.register(Pedido)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Movimentacao)
admin.site.register(Financeiro)
