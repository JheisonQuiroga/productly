from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from productos.forms import ProductoForm
from .models import Producto

# Create your views here.

# /productos


def index(request):
    productos = Producto.objects.all()

    # Retornamos la funcion de render, ya disponible en la creacion
    # del archivo de views o cuando creamos las aplicaciones
    return render(
        request,
        'index.html',
        context={'productos': productos}
    )


def detalle(request, producto_id):
    # El primer argumento que recibe es la clase que va a utilizar,
    # El segundo es como vamos a buscar el elemento
    producto = get_object_or_404(Producto, id=producto_id)

    return render(
        request,
        'detalle.html',
        context={'producto': producto}
    )


def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')

    else:
        form = ProductoForm()

    return render(
        request,
        'producto_form.html',
        {'form': form}
    )
