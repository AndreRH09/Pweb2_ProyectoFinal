from django.urls import include, path
from . import views

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', views.index, name = 'index'),
    path('produtos/', views.ProductoListView.as_view(), name = 'productos'),
    path('categorias/', views.CategoriaListView.as_view(), name = 'categorias'),
    path('produto/<int:pk>', views.ProductoDetailView.as_view(), name='producto'),
    path('pedidos/', views.PedidoListView.as_view(), name = 'pedidos'),# falta implementar
    path('addCliente/', views.clienteCreateView, name = 'addcliente'),
    path('apiRest/', include('rest_framework.urls')),
    path('a/', include(router.urls), name='administrar'),
]