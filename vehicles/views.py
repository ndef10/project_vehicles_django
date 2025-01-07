from django.shortcuts import render, redirect
from vehicles.models import Vehiculo

# Create your views here.
def v_index(request):
    return render(request, 'vehicles/index.html')

def v_add(request):
    if request.method == 'POST':
        data = request.POST.copy()
        vehiculo = Vehiculo()

        vehiculo.marca = data['marca']
        vehiculo.modelo = data['modelo']
        vehiculo.serial_carroceria = data['serial_carroceria']
        vehiculo.serial_motor = data['serial_motor']
        vehiculo.categoria = data['categoria']
        vehiculo.precio = data['precio']
        vehiculo.fecha_creacion = data['fecha_creacion']
        vehiculo.fecha_modificacion = data['fecha_modificacion']
        
        vehiculo.save()
        return redirect('/')
    return render(request, 'vehicles/add.html')

def v_listar(request):
    vehiculos = Vehiculo.objects.all()
    context = {
        'vehiculos': vehiculos
    }
    return render(request, 'vehicles/listar.html', context)