from django.shortcuts import render, HttpResponse, redirect
from .models import Periodista
from datetime import datetime
from .forms import PeriodistaForm
from .forms import PeriodistaForm2
from .models import Producto
from .carrito import Carrito


def home(request):
    return render(request, "core/home.html")


def nosotros(request):
    return render(request, "core/nosotros.html")


def contacto(request):
    return render(request, "core/contacto.html")


def sesion(request):
    return render(request, "core/sesion.html")


def carrito(request):
    return render(request, "core/carrito.html")


def productos(request):
    return render(request, "core/productos.html")


def periodistas(request):
    periodistas = Periodista.objects.all()

    if request.method == "POST":
        periodistaForm = PeriodistaForm(request.POST, request.FILES)

        if periodistaForm.is_valid():
            periodistaForm.save()
            return redirect('periodistas')
    else:
        periodistaForm = PeriodistaForm()

    return render(request, 'core/periodistas.html', {"periodistas": periodistas, 'periodistaForm': periodistaForm})


def editarPeriodista(request, codigo):
    periodista = Periodista.objects.get(codigo=codigo)
    periodistaForm = PeriodistaForm2(instance=periodista)
    if request.method == 'POST':
        formulario = PeriodistaForm2(request.POST, instance=periodista)

        if formulario.is_valid():
            formulario.save()
            return redirect('periodistas')

    return render(request, 'core/editarPeriodista.html', {'periodistaForm': periodistaForm})


def eliminarPeriodista(request, codigo):
    periodistas = Periodista.objects.get(codigo=codigo)
    periodistas.delete()

    return redirect('periodistas')


def tienda(request):
    productos = Producto.objects.all()
    return render(request, "core/productos.html", {'productos': productos})


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("productos.html")


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("productos.html")


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("productos.html")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("productos.html")
