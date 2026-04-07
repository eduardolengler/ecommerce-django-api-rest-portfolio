from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from loja.views import ProdutoViewSet, ClienteViewSet, PedidoViewSet # Importe a nova view
from rest_framework import permissions 
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

# Configuração dos Metadados da API (Nome, contato, licença)
schema_view = get_schema_view(
   openapi.Info(
      title="API E-commerce TCC",
      default_version='v1',
      description="Documentação técnica da API de vendas desenvolvida para o TCC.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="eduardo@tcc.com.br"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Importe as views do JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Cria o roteador e registra a view
router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet, basename='pedido')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Todas as rotas da API começam com 'api/'

    # Rotas de Autenticação
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Renovar token

    # Rota do Swagger (O site da documentação)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

