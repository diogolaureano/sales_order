from django.shortcuts import render # type: ignore
from .models import Pedido
from .models import Movimentacao

# Create your views here.

def home(request):
    return render(request, 'pedidos/home.html')

def pedidos(request):
    #Salvar os dados no banco
    novo_pedido = Pedido()
    novo_pedido.id_pedido = novo_pedido.id_pedido 
    novo_pedido.data_da_venda = request.POST.get('data_da_venda')
    novo_pedido.cliente = request.POST.get('cliente')
    novo_pedido.produto = request.POST.get('produto')
    novo_pedido.quantidade = request.POST.get('quantidade')
    novo_pedido.valor_de_venda = request.POST.get('valor_de_venda')
    novo_pedido.taxas = request.POST.get('taxas')
    novo_pedido.valor_liquido = request.POST.get('valor_liquido')
    novo_pedido.prazo = request.POST.get('prazo')
    novo_pedido.canal_de_venda = request.POST.get('canal_de_venda')
    novo_pedido.codigo_de_rastreio = request.POST.get('codigo_de_rastreio')
    novo_pedido.save()

    #Exibir pedidos 
    pedidos = {
        'pedidos': Pedido.objects.all()
        
    }
       
    #Retornar o dados para a pagina
    return render(request,'pedidos/pedidos.html',pedidos)