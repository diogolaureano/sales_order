from django.shortcuts import render # type: ignore
from .models import Pedido

# Create your views here.

def home(request):
    return render(request, 'pedidos/home.html')

def pedidos(request):
    #Salvar os dados no banco
    novo_pedido = Pedido()
    novo_pedido.pedido = request.POST.get('pedido')
    novo_pedido.cliente = request.POST.get('cliente')
    novo_pedido.save()

    #Exibir pedidos 
    pedidos = {
        'pedidos': Pedido.objects.all()
    }

    #Retornar o dados para a pagina
    return render(request,'pedidos/pedidos.html',pedidos)