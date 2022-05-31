from django.shortcuts import render , redirect
from .models import Libro
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required

def home(request):
    librosListados= Libro.objects.all()
    messages.success(request, '¡Libros listados!')
    return render(request, "gestionLibros.html",{"libros":librosListados})


def registrarLibro(request):
    codigo=request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    autor = request.POST['txtAutor']
    editorial = request.POST['txtEditorial']
    año = request.POST['txtAño']

    libro=Libro.objects.create(
        codigo=codigo,nombre=nombre,autor=autor,editorial=editorial,año=año)
    messages.success(request, '¡Libro registrado!')
    return redirect('/')
def edicionLibro(request,codigo):
    libro = Libro.objects.get(codigo=codigo)
    return render(request, "edicionLibro.html", {"libro": libro})

def editarLibro(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    autor = request.POST['txtAutor']
    editorial = request.POST['txtEditorial']
    año = request.POST['txtAño']

    libro = Libro.objects.get(codigo=codigo)
    libro.nombre=nombre
    libro.autor=autor
    libro.editorial=editorial
    libro.año=año
    libro.save()
    messages.success(request, '¡Libro actualizado!')

    return redirect('/')


def eliminacionLibro(request, codigo):
    libro= Libro.objects.get(codigo=codigo)
    libro.delete()
    messages.success(request, '¡Libro eliminado!')
    return redirect('/')


def salir(request):
    logout(request)
    return redirect('/')