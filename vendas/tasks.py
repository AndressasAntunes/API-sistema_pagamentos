from celery import shared_task
from .models import Cliente, Produto, Notificacao


@shared_task
def criar_notificacao(cliente_id, produto_id):

    cliente = Cliente.objects.get(id=cliente_id)
    produto = Produto.objects.get(id=produto_id)

    Notificacao.objects.create(
        cliente=cliente,
        produto=produto,
        mensagem=f'O preço do produto {produto.descricao} diminuiu.'
    )

    return 'Notificação criada'