from django import forms
from .models import Livro
from .models import Cliente


class ClienteForms(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'CPF',
            'telefone',
            'endereco'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control text-red',
                'placeholder': 'digite seu nome'
            }),

            'CPF': forms.TextInput(attrs={
                'class': 'form-control text-red',
                'placeholder': 'digite seu cpf'
            }),

            'telefone': forms.TextInput(attrs={
                'class': 'form-control text-red',
                'placeholder': 'digite seu telefone'
            }),

            'endereco': forms.TextInput(attrs={
                'class': 'form-control text-red',
                'placeholder': 'digite seu endereco'
            })
        }


class livroForms(forms.ModelForm):
    class Meta:
        model = Livro
        fields = [
            'titulo',
            'autor',
            'editora',
            'ano_publicacao',
            'isbn',
            'genero',
            'quantidade'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control text-red',
                'placeholder': 'Digite o nome do livro'
            }),

            'autor': forms.TextInput(attrs={
                'class': 'form-control text-red',
                'placeholder': 'Digite o nome do autor'

            }),

            'editora': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome da editora'
            }),
        }
