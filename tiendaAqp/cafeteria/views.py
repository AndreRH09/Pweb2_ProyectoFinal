from django.shortcuts import render
from django.views import generic
from .models import * # cliente, categoria, producto, pedido, itempedido, carrito, itemcarrito, reserva

# Create your views here.

def index(request):
    num_categoria = Categoria.objects.all().count()
    num_producto = Producto.objects.all().count()
    num_cliente = Cliente.objects.count()
    num_pendiente = Pedido.objects.filter(estado='P').count()

    icono = ('bi bi-hand-thumbs-up', 'bi bi-check2-square', 'bi bi-hourglass')
    caracteristica = ('Compromiso', 'Seguridad', 'Eficacia')
    descripcion_caracteristica = (
        'Tendrás tus pedidos sin falta',
        'Tus pedidos se preparan con todos los protocolos de seguridad',
        'Sabemos que tu tiempo es valioso',
    )
    
    caracteristicas_combinadas = zip(icono, caracteristica, descripcion_caracteristica)

    context = {
        'caracteristicas_combinadas': caracteristicas_combinadas,
        'num_categoria': num_categoria,
        'num_producto': num_producto,
        'num_cliente': num_cliente,
        'num_pendiente': num_pendiente,
    }

    return render(request, 'index.html', context=context)

class CategoriaListView(generic.ListView):
    model = Categoria
    
    context_object_name = 'categoria_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categorias = Categoria.objects.all()
        context['categorias'] = categorias
        return context

class ProductoListView(generic.ListView):
    model = Producto

    context_object_name = 'producto_list'

    def get_context_data(self, **kwargs):
        context = super(ProductoListView, self).get_context_data(**kwargs)
        context['uno contexto'] = 'algo más'
        return context
    
    def get_queryset(self):
        return Producto.objects.all() #filter(title__icontains='war')[:5]
    
    #template_name = 'books/my_arbitrary_template_name_list.html'

class ReservaMesaListView(generic.ListView):
    model = ReservaMesa

class PedidoListView(generic.ListView):
    model = Pedido