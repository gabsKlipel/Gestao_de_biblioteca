from django import forms
from .models import Livro, Cliente


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
            'quantidade',
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


            'ano_publicacao': forms.NumberInput(attrs={
                'placeholder': 'Ex: 2023',
                'min': '1600',
                'max': '2030'
            }),

        }


class clienteForms(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'cpf',
            'telefone',
            'endereco'
        ]

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control text-red',
                'placeholder': 'Digite o nome do cliente'
            }),

            'cpf': forms.TextInput(attrs={
                'class': 'form-control text-red',
                'placeholder': 'Digite o cpf do cliente'
            }),

            'telefone': forms.TextInput(attrs={
                'class': 'form-control text-red',
                'placeholder': 'Digite o telefone do cliente'
            }),

            'endereco': forms.TextInput(attrs={
                'class': 'form-control text-red',
                'placeholder': 'Digite o endereco do cliente'
            }),

        }
