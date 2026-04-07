from django.contrib import admin
from .models import Produto, Pedido, ItemPedido

# Configuração para ver os itens DENTRO da tela do pedido
class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]
    list_display = ['id', 'cliente', 'data_pedido', 'status']

admin.site.register(Produto) # Isso faz o modelo aparecer na tela de admin
admin.site.register(Pedido, PedidoAdmin) # Não precisa registrar ItemPedido separado, ele vai aparecer dentro do Pedido
