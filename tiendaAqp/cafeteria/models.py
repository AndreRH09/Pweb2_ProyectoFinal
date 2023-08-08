from django.db import models
from django.urls import reverse

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['nombre']

    def get_absolute_url(self):
        return reverse('cliente-detail', args=[str(self.id)])


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='cafeteria/static/img/productos')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('producto', args=[str(self.id)]) # debe ser igual a name de view
    
    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField('Producto', through='ItemPedido')
    ESTADOS_PEDIDO = [
        ('P', 'Pendiente'),
        ('E', 'En preparación'),
        ('C', 'Completado'),
    ]
    estado = models.CharField(max_length=1, choices=ESTADOS_PEDIDO, default='P')

    def get_estado_display(self):
        return dict(self.ESTADOS_PEDIDO)[self.estado]
    
    def total_monto(self, obj):
        return sum(item.subtotal() for item in obj.itempedido_set.all())
    
    def __str__(self):
        return f"Pedido {self.cliente} - {self.id}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def subtotal(self):
        return self.cantidad * self.producto.precio

    def __str__(self):
        return f"Pedido {self.producto.nombre}, Cantidad {self.cantidad}, Precio unitario {self.producto.precio}"


class Carrito(models.Model):
    cliente = models.OneToOneField('Cliente', on_delete=models.CASCADE)
    productos = models.ManyToManyField('Producto', through='ItemCarrito')

    def __str__(self):
        return f"Carrito de {self.cliente.nombre}"


class ItemCarrito(models.Model):
    carrito = models.ForeignKey('Carrito', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre} en {self.carrito}"


class ReservaMesa(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.PositiveIntegerField()

    def __str__(self):
        return f"Reserva para {self.cantidad_personas} personas el {self.fecha} a las {self.hora}"