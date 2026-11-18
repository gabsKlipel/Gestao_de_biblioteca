from django.shortcuts import render, redirect
from .forms import livroForms, clienteForms
from django.contrib import messages
from .models import Livro, Emprestimo, Cliente
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm

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

    dados = {
        'formulario': form
    }

    return render(request, "cadastrar_livro.html", dados)


def listar_livros(request):
    ordem = request.GET.get('ordem', 'titulo')
    nome_da_pesquisa = request.GET.get('pesquisa', '')

    livro = Livro.objects.filter(
        titulo__icontains=nome_da_pesquisa,
        ativo=True

    ).order_by(ordem)

    dados = {
        'livros': livro,
        nome_da_pesquisa: nome_da_pesquisa,
    }

    return render(request, "listar_livros.html", dados)


def devolver_livro(request, id):
    livro = Livro.objects.get(id=id)

    emprestimo_ativo = Emprestimo.objects.filter(
        livro=livro, status=False).first()

    if emprestimo_ativo:
        emprestimo_ativo.status = True
        emprestimo_ativo.save()
        livro.quantidade += 1
        livro.emprestado = False
        livro.save()
        messages.success(
            request, f'O livro "{livro.titulo}" foi devolvido com sucesso!')
    else:

        messages.error(
            request, f'Não há empréstimos ativos para o livro "{livro.titulo}".')

    return render(request, 'listar_livros.html')


def emprestar_livro(request, id):
    livro = Livro.objects.get(id=id)

    if request.method == 'POST':
        if livro.quantidade <= 0:
            messages.warning(
                request, f'O livro "{livro.titulo}" já está emprestado.')
            return redirect('listar_livros')

        data_str = request.POST.get('data_devolucao')

        if data_str:
            data_devolucao = datetime.strptime(data_str, '%Y-%m-%d').date()

            livro.emprestado = True
            livro.quantidade -= 1
            livro.save()

            emprestimo = Emprestimo(
                livro=livro,
                data_devolucao=data_devolucao,
                data_emprestimo=timezone.now().date(),

                status=False
            )
            emprestimo.save()

            messages.success(
                request, f'Emprestado com sucesso! Devolver em: {data_devolucao.strftime("%d/%m/%Y")}')
            return redirect('listar_livros')
        else:
            messages.error(request, "Informe a data de devolução.")

    return render(request, 'emprestar_livro.html', {'livro': livro})


def editar_livro(request, id):
    livro = Livro.objects.get(id=id)

    form = livroForms(instance=livro)

    if request.method == 'POST':

        form = livroForms(request.POST, instance=livro)

        if form.is_valid():
            form.save()
            titulo = form.cleaned_data['titulo']

            mensagem_confirmacao = f'livro {titulo} alterado com sucesso!'
            messages.success(request, mensagem_confirmacao)

            return redirect('listar_livros')

    dados = {
        'formulario': form
    }
    return render(request, 'editar_livro.html', dados)


def desativar_livro(request, id):
    livro = Livro.objects.get(id=id)
    titulo = livro.titulo
    livro.ativo = False
    livro.save()
    messages.success(
        request, f'{titulo} foi desativado com sucesso'
    )
    return redirect('listar_livros')


def ativar_livro(request, id):
    livro = Livro.objects.get(id=id)
    titulo = livro.titulo
    livro.ativo = True
    livro.save()
    messages.success(
        request, f'{titulo} foi ativado com sucesso'
    )
    return redirect('listar_livros')


def livros_inativos(request):
    livro = Livro.objects.filter(
        ativo=False
    )
    dados = {
        'livros': livro
    }
    return render(request, 'livros_inativos.html', dados)


def excluir_livro(request, id):
    livro = Livro.objects.get(id=id)
    titulo = livro.titulo
    if livro.quantidade > 0:
        messages.error(
            request, 'impossivel excluir um livro que possui estoque')
        return redirect('livros_inativos')
    else:
        livro.delete()
        messages.success(request, f'{titulo} excluido com sucesso')
    return redirect('listar_livros')


def cadastrar_cliente(request):
    form = clienteForms()

    dados = {
        'formulario': form
    }

    if request.method == 'POST':
        form = clienteForms(request.POST)
        if form.is_valid():
            form.save()
            nome = form.cleaned_data['nome']
            mensagem_confirmacao = f'Cliente {nome} cadastrado com sucesso!'
            messages.success(request, mensagem_confirmacao)
            return redirect('index')

    dados = {
        'formulario': form
    }

    return render(request, "cadastrar_cliente.html", dados)


def listar_cliente(request):
    ordem = request.GET.get('ordem', 'nome')
    nome_da_pesquisa = request.GET.get('pesquisa', '')

    cliente = Cliente.objects.filter(
        nome__icontains=nome_da_pesquisa,
        ativo=True

    ).order_by(ordem)

    dados = {
        'clientes': cliente,
        nome_da_pesquisa: nome_da_pesquisa,
    }

    return render(request, "listar_cliente.html", dados)


def desativar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    nome = cliente.nome
    cliente.ativo = False
    cliente.save()
    messages.success(
        request, f'{cliente} foi desativado com sucesso'
    )
    return redirect('listar_cliente')


def clientes_inativos(request):
    cliente = Cliente.objects.filter(
        ativo=False
    )
    dados = {
        'clientes': cliente
    }
    return render(request, 'clientes_inativos.html', dados)


def ativar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    nome = cliente.nome
    cliente.ativo = True
    cliente.save()
    messages.success(
        request, f'{nome} foi ativado com sucesso'
    )
    return redirect('listar_cliente')


def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    form = clienteForms(instance=cliente)

    if request.method == 'POST':

        form = clienteForms(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            nome = form.cleaned_data['nome']

            mensagem_confirmacao = f'livro {nome} alterado com sucesso!'
            messages.success(request, mensagem_confirmacao)

            return redirect('listar_cliente')

    dados = {
        'formulario': form
    }
    return render(request, 'editar_livro.html', dados)


def excluir_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    nome = cliente.nome
    cliente.delete()
    messages.success(request, f'{nome} excluido com sucesso')
    return redirect('listar_cliente')


def cadastrar_funcionario(request):
    if request.method == 'POST':
        formulario_de_usuario = UserCreationForm(request.POST)

        if formulario_de_usuario.is_valid():
            formulario_de_usuario.save()
            usuario = formulario_de_usuario.cleaned_data['username']
            messages.success(
                request, f'Funcionario {usuario} cadastrado com sucesso!')
            return redirect('cadastrar_funcionario')
    else:
        formulario_de_usuario = UserCreationForm()

    dados = {
        'formulario': formulario_de_usuario
    }
    return render(request, "cadastrar_funcionario.html", dados)
