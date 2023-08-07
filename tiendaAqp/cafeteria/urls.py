from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('produtos/', views.ProductoListView.as_view(), name = 'productos'),
    path('categorias/', views.CategoriaListView.as_view(), name = 'categorias'),
    path('produtos/<int:pk>', views.ProductoDetailView.as_view(), name='producto'),
]