from django.db import models
from isbn_field import ISBNField


# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    isbn = ISBNField(clean_isbn=True)
    genero = models.CharField(max_length=100, null=True, blank=True)
    quantidade = models.IntegerField(default=1)
    emprestado = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateField(blank=False, null=False)
    status = models.BooleanField(default=False)


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
