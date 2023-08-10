from django.urls import include, path
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'pedidos', views.PedidoViewSet)


urlpatterns = [
    path('', views.index, name = 'index'),
    path('produtos/', views.ProductoListView.as_view(), name = 'productos'),
    path('categorias/', views.CategoriaListView.as_view(), name = 'categorias'),
    path('produto/<int:pk>', views.ProductoDetailView.as_view(), name='producto'),
    path('pedidos/', views.PedidoListView.as_view(), name = 'pedidos'),
    path('addCliente/', views.clienteCreateView, name = 'addcliente'),
    path('pedir/', views.pedidoCreateView, name='hacer_pedido'),
    #paraoteraciones crud
    path('apiRest/', include('rest_framework.urls')),
    path('administracion/', include(router.urls), name='administrar'),
    path('doc/', include_docs_urls(title='documentacion')),
]