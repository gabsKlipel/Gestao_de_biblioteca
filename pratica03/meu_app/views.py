from django.shortcuts import render, redirect
from .forms import livroForms

# Create your views here.


def index(request):

    return render(request, "index.html")


def cadastrar_livro(request):
    form = livroForms()

    dados = {
        'formulario': form
    }

    if request.method == 'POST':
        form = livroForms(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            return redirect('index')

    return render(request, "cadastrar_livro.html", dados)

def cadastrar_usuario(request):
     
    return render(request, "cadastrar_usuario.html")