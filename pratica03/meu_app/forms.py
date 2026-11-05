from django import forms
from .models import Livro

class livroForms(forms.ModelForm):
    class meta:
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