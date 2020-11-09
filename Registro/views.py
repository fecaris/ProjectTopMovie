from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioForm
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.
def Usuario_list(request):
    usuarios = Usuario.objects.all()
    #antes era Registro/Usuario_list.html'
    return render(request, 'Registro/Usuario_list_ext.html', {'lista_Usuarios': usuarios})

def menu(request):
    return render(request, 'Registro/menu.html',{})

def top2020(request):
    return render(request, 'Registro/top2020.html',{})

def top2019(request):
    return render(request, 'Registro/top2019.html',{})

def noticias(request):
    return render(request, 'Registro/noticias.html',{})


#USUARIO
def usuario_detail(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'Registro/usuario_detail.html', {'usuario': usuario})

#crear nuevo usuario
def usuario_new(request):
    form = UsuarioForm()
    return render(request, 'Registro/registroUsuario.html',{'form': form})

#esto aun no esta listo 
def usuario_edit(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if usuario.is_valid():
            usuario = form.save(commit=False)
            usuario.author = request.user
            usuario.published_date = timezone.now()
            usuario.save()
            return redirect('usuario_detail', pk=usuario.pk)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'Registro/usuario_edit.html', {'form': form})
