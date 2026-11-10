from django.shortcuts import render, redirect
from .forms import livroForms
from django.contrib import messages
from .models import Livro

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
            form.save()
            titulo = form.cleaned_data['titulo']
            mensagem_confirmacao = f'Livro {titulo} cadastrado com sucesso!'
            messages.success(request, mensagem_confirmacao)
            return redirect('index')

    return render(request, "cadastrar_livro.html",dados)

def listar_livros(request):
    ordem = request.GET.get('ordem', 'titulo')
    nome_da_pesquisa = request.GET.get('pesquisa', '')

    livro = Livro.objects.filter(
        titulo__icontains=nome_da_pesquisa,
        
        ).order_by(ordem)
    
    dados = {
        'livros': livro,    
        nome_da_pesquisa: nome_da_pesquisa,
    }

    return render(request, "listar_livros.html", dados) 