from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    # Definindo as colunas da tabela
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='fotos_produtos/', null=True, blank=True)

    def __str__(self):
        return self.nome
    

class Pedido(models.Model):
    # Status possível para a máqna de estados
    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('A', 'Aprovado'),
        ('E', 'Enviado'),
        ('C', 'Cancelado'),
    ]

    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos')
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.username}"
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(default=1)
    preco_no_ato = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"