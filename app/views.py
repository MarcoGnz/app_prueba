from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import articulo
from .forms import EjemploForm

def hola_mundo(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def crear_articulo(request):
    if request.method == 'POST':
        form = EjemploForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_articulos')
    else:
        form = EjemploForm()
    return render(request, 'app/crear_articulo.html', {'form': form})

def lista_articulos(request):
    Articulos = articulo.objects.all()
    return render(request, 'app/lista_articulos.html', {'articulos': Articulos})

def editar_articulo(request, id):
    Articulo = get_object_or_404(articulo, id=id)
    if request.method == 'POST':
        form = EjemploForm(request.POST, instance=Articulo)
        if form.is_valid():
            form.save()
            return redirect('lista_articulos')
    else:
        form = EjemploForm(instance=articulo)
    return render(request, 'app/editar_articulo.html', {'form': form, 'articulo': Articulo})

def eliminar_articulo(request, id):
    Articulo = get_object_or_404(articulo, id=id)   
    if request.method == 'POST':
        Articulo.delete()
        return redirect('lista_articulos')
    return render(request, 'app/eliminar_articulo.html', {'articulo': Articulo})
