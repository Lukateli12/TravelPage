from django.shortcuts import render
from . forms import UsuarioForm

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def libros(request):
    return render(request, 'paginas/index.html')
def comprar(request):
    return render(request, 'paginas/formulario.html')
def formulario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()
    return render(request, 'formulario.html', {'form': form})