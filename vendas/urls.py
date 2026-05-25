from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'clientes', ClienteViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'condicoes', CondicaoPagamentoViewSet)
router.register(r'precos', PrecoClienteViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'itens', ItemVendaViewSet)
router.register(r'notificacoes', NotificacaoViewSet)

urlpatterns = router.urls