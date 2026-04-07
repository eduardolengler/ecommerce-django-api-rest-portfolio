from rest_framework import serializers
from .models import Produto
from django.contrib.auth.models import User
from .models import Pedido, ItemPedido

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        # Importante: A senha nunca deve voltar na resposta da API (segurança)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Uso do create_user para que o Django faça o hash da senha automaticamente
        user = User.objects.create_user(**validated_data)
        return user
    
class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ['produto', 'quantidade', 'preco_no_ato']
        # O preço é somente leitura (quem define é o sistema, não o usuário)
        read_only_fields = ['preco_no_ato']

class PedidoSerializer(serializers.ModelSerializer):
    # Permite enviar uma lista de itens dentro do JSON do pedido
    itens = ItemPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'data_pedido', 'status', 'itens']
        # O cliente será pego automaticamente do usuário logado
        read_only_fields = ['cliente', 'status']

    def create(self, validated_data):
        # 1. Separa os itens do resto dos dados
        itens_data = validated_data.pop('itens')
        
        # 2. Cria o Pedido vazio
        pedido = Pedido.objects.create(**validated_data)
        
        # 3. Cria cada Item do Pedido
        for item in itens_data:
            produto = item['produto']
            quantidade = item['quantidade']
            # REGRA DE NEGÓCIO: Pega o preço atual do produto no banco
            preco_atual = produto.preco 
            
            ItemPedido.objects.create(
                pedido=pedido,
                produto=produto,
                quantidade=quantidade,
                preco_no_ato=preco_atual
            )
            
        return pedido