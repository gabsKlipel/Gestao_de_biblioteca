from django.db import models
from isbn_field import ISBNField

# Create your models here.

class Livro (models.Model):
    titulo = models.CharField(max_length = 100),
    autor = models.CharField(max_length = 100),
    editora = models.CharField(max_length = 100),
    ano_publicacao = models.DateField(),
    isbn = ISBNField(clean_isbn = True),
    genero = models.CharField(max_length = 100),
    quantidade = models.IntegerField()

    def __str__(self):
        return self.titulo