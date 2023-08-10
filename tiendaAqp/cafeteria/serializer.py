from rest_framework import serializers
from .models import Producto, Categoria, Pedido
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['url', 'username', 'email', 'is_staff']
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Categoria
        fields = '__all__' # todos los campos

class ProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Producto
        # fields = ('nombre', 'descripcion', 'precio')
        fields = '__all__' # todos los campos

class PedidoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Pedido
        fields = '__all__' # todos los campos
