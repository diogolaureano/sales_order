from django.contrib import admin
from .models import Pedido
from .models import Movimentacao

# Register your models here.
admin.site.register(Pedido)
admin.site.register(Movimentacao)