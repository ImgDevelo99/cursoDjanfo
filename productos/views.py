from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.
#funcion que se encarga de mostrar una lista de productos
def listar_productos(request):#request representa una solicitud http
    productos = Producto.objects.all()#consultar todos los registros de tabla producto
    return render(request, 'productos/listar.html', {'productos': productos})

#--------------------------------------------
#funcion crear producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
        return render(request, 'producto/crear.html', {'form': form})