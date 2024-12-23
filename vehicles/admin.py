from django.contrib import admin
from .models import Vehiculo

# Register your models here.

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'categoria', 'precio', 'fecha_creacion')
    search_fields = ('marca', 'modelo', 'serial_carroceria', 'serial_motor')
    list_filter = ('marca', 'categoria')
