#from django.shortcuts import render
from rest_framework import viewsets
from .models import Produto
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, AllowAny
from .serializers import ProdutoSerializer, ClienteSerializer, PedidoSerializer # Importa o novo serializer
from .models import Pedido


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all() # Busca todos os produtos no banco
    serializer_class = ProdutoSerializer # Usa o tradutor criado
    #permission_classes = [IsAuthenticated] # Produtos: Só quem tem token pode ver ou editar (Padrão de segurança)
    permission_classes = [AllowAny] # Libera para o React ver os Produtos

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ClienteSerializer

    def get_permissions(self):
        # Se a ação for 'create' (cadastro), permite qualquer um
        if self.action == 'create':
            permission_classes = [AllowAny]
        # Para listar ou deletar, exige ser Admin
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated] # Só clientes logados podem comprar

    def get_queryset(self):
        # REGRA DE SEGURANÇA:
        # Usuário comum só vê os SEUS pedidos.
        # Admin vê TODOS.
        user = self.request.user
        if user.is_staff:
            return Pedido.objects.all()
        return Pedido.objects.filter(cliente=user)

    def perform_create(self, serializer):
        # Define automaticamente o cliente como o usuário logado
        serializer.save(cliente=self.request.user)