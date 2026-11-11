from django.shortcuts import render, redirect
from .forms import livroForms, ClienteForms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

# Create your views here.


def index(request):

    return render(request, "index.html")

@login_required
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
            return redirect('index')

    return render(request, "cadastrar_livro.html", dados)


@login_required
def cadastrar_cliente(request):
    form = ClienteForms()

    dados = {
        'formulario': form
    }

    if request.method == 'POST':
        form = ClienteForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, "cadastrar_cliente.html", dados)

def cadastrar_usuario(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = UserCreationForm()
    dados = {
        'formulario': form
    }
    return render(request, 'cadastrar_usuario.html', dados)

