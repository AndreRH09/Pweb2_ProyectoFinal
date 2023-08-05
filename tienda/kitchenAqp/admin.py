from django.contrib import admin
from .models import comidas
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "tipo"]
   

admin.site.register(comidas, ProductAdmin)
