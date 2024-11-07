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
def crear_producto(request):#solicitud de http
    if request.method == 'POST':# verifica el metodo de solicitud es POST
        form = ProductoForm(request.POST)# se cargan los datos enviados por el usuario al formulario
        if form.is_valid(): #verifica si los datos en el formulario son validos
            form.save()# guardar los datos en el bd
            return redirect('listar_productos')# me retorna a la vista listar productos
    else:
        form = ProductoForm()
        return render(request, 'producto/crear.html', {'form': form})
#-----------------------------------------------
# funcion editar producto
def editar_producto(request, producto_id): #ID del producto que quiero editar
    producto = Producto.object.get(id = producto_id)# se busca en la bd el id,
    if  request.method == "POST":# verifica el metodo de solicitud post
        form = ProductoForm(request.POST, instance=producto)# indica al formulario que los datos ingresados deben actualizar el objeto producto
        if form.is_valid(): #verifica si los datos en el formulario son validos
            form.save()# guardar los datos en el bd
            return redirect('listar_productos')# me retorna a la vista listar productos
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'producto/editar.html', {'form': form})

#-------------------------------------------------
def eliminar_producto(request, producto_id):
    producto = Producto.object.get(id = producto_id)# se busca en la bd el id,
    if  request.method == "POST":# verifica el metodo de solicitud post
        producto.delete()
        return redirect("listar_productos")
    return render(request, 'producto/eliminar.html', {'producto': producto})


    # post : se usa para enviar datos al servidor
    # Get : se usa para solicitar datos al servidor
    # Put : se usa para actualizar o editar un recurso completo en el servidor
    # Delete : se emplea para eliminar un recurso en el servidor