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
    fields = ['nombre', ('email', 'telefono')]

#
@admin.register(Producto)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'imagen')
    list_filter = ('categoria', 'precio')
    fieldsets = (
        (None, {
            'fields': ('nombre', 'descripcion')
        }),
        ('extra', {
            'fields': ['imagen', ('precio', 'categoria')]
        }),
    )

#
class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

@admin.register(Pedido)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'total_items', 'total_monto', 'estado')
    inlines = [ItemPedidoInline]

    def total_items(self, obj):
        return ', '.join(producto.nombre for producto in obj.productos.all()[:3])
    total_items.short_description = 'Productos'

    def total_monto(self, obj):
        return sum(item.subtotal() for item in obj.itempedido_set.all())
    total_monto.short_description = 'Total Monto'

#
@admin.register(ItemPedido)

class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad', 'precio', 'total_monto')

    def precio(self, obj):
        return obj.producto.precio
    precio.short_description = 'Precio unitario'

    def total_monto(self, instance):
        return instance.subtotal()
    total_monto.short_description = 'Total Monto'

#
class ItemCarritoInline(admin.TabularInline):
    model = ItemCarrito
    extra = 1
    
@admin.register(Carrito)

class CarritoAdmin(admin.ModelAdmin):

    list_display = ('cliente', 'display_producto')
    inlines = [ItemCarritoInline]

    def display_producto(self, obj):
        return ', '.join(producto.nombre for producto in obj.productos.all()[:3])
    display_producto.short_description = 'Productos'
    
#
@admin.register(ItemCarrito)

class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ('carrito', 'producto', 'cantidad')

#
@admin.register(ReservaMesa)

class ReservaMesaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'hora')
