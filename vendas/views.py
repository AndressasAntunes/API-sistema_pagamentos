from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import *
from .serializers import *
from .tasks import criar_notificacao


class PrecoClienteViewSet(viewsets.ModelViewSet):

    queryset = PrecoCliente.objects.all()
    serializer_class = PrecoClienteSerializer

    def create(self, request, *args, **kwargs):

        response = super().create(request, *args, **kwargs)

        preco = PrecoCliente.objects.last()

        criar_notificacao.delay(
            preco.cliente.id,
            preco.produto.id
        )

        return response

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    @action(detail=False, methods=['get'])
    def relatorio(self, request):

        cnpj = request.GET.get('cnpj')
        razao = request.GET.get('razao_social')

        clientes = Cliente.objects.all()

        if cnpj:
            clientes = clientes.filter(cnpj=cnpj)

        if razao:
            clientes = clientes.filter(razao_social__icontains=razao)

        resultado = []

        for cliente in clientes:

            vendas = Venda.objects.filter(cliente=cliente)

            lista_vendas = []

            for venda in vendas:

                itens = ItemVenda.objects.filter(venda=venda)

                lista_itens = []

                for item in itens:
                    lista_itens.append({
                        "produto": item.produto.descricao,
                        "quantidade": item.quantidade,
                        "preco_unitario": float(item.preco_unitario)
                    })

                lista_vendas.append({
                    "venda_id": venda.id,
                    "valor_total": float(venda.valor_total),
                    "itens": lista_itens
                })

            resultado.append({
                "cliente": cliente.razao_social,
                "cnpj": cliente.cnpj,
                "vendas": lista_vendas
            })

        return Response(resultado)


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CondicaoPagamentoViewSet(viewsets.ModelViewSet):
    queryset = CondicaoPagamento.objects.all()
    serializer_class = CondicaoPagamentoSerializer


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer


class ItemVendaViewSet(viewsets.ModelViewSet):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer


class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer