from django.db import models
from isbn_field import ISBNField

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=100, null = True,blank = True)
    autor = models.CharField(max_length=100, null=True, blank=True)
    editora = models.CharField(max_length=100, null=True, blank=True)
    ano_publicacao = models.DateField(null=True, blank=True)
    isbn = ISBNField(clean_isbn=True, null=True, blank=True)
    genero = models.CharField(max_length=100, null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.titulo