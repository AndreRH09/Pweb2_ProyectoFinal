from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('produtos/', views.ProductoListView.as_view(), name = 'productos'),
    path('categorias/', views.CategoriaListView.as_view(), name = 'categorias'),
    path('produto/<int:pk>', views.ProductoDetailView.as_view(), name='producto'),
    path('pedidos/', views.PedidoListView.as_view(), name = 'pedidos'),
]