from django.contrib import admin
from .models import Cliente, Produto, CondicaoPagamento, PrecoCliente, Venda, ItemVenda, Notificacao

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(CondicaoPagamento)
admin.site.register(PrecoCliente)
admin.site.register(Venda)
admin.site.register(ItemVenda)
admin.site.register(Notificacao)