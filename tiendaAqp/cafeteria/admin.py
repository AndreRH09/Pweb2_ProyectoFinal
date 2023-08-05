from django.contrib import admin
from .models import *

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categoria, CategoriaAdmin)

#
@admin.register(Cliente)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')

#
@admin.register(Producto)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'imagen')

#
@admin.register(Pedido)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'estado')

#
@admin.register(ItemPedido)

class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad', 'precio_unitario')

#
@admin.register(Carrito)

class CarritoAdmin(admin.ModelAdmin):
    pass

#
@admin.register(ItemCarrito)

class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ('carrito', 'producto', 'cantidad')

#
@admin.register(ReservaMesa)

class ReservaMesaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'hora')
