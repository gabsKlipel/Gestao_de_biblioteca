from django.shortcuts import render
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

    return render(request, "cadastrar_livro")
