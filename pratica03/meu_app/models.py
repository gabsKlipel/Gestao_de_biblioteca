from django.db import models
from isbn_field import ISBNField

# Create your models here.


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.DateField(blank=True, null=True)
    isbn = ISBNField(clean_isbn=True)
    genero = models.CharField(max_length=100)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.titulo


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=11)
    telefone = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
