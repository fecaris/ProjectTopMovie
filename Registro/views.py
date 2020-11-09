from django.shortcuts import render
from .models import Usuario

# Create your views here.
def Usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'Registro/Usuario_list.html', {'lista_Usuarios': usuarios})

def menu(request):
    return render(request, 'Registro/menu.html',{})

def top2020(request):
    return render(request, 'Registro/top2020.html',{})

def top2019(request):
    return render(request, 'Registro/top2019.html',{})

def noticias(request):
    return render(request, 'Registro/noticias.html',{})
