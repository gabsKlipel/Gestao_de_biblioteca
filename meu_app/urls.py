from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('cadastrar_livro/', views.cadastrar_livro, name = 'cadastrar_livro'),
    path('listar_livros/', views.listar_livros, name = 'listar_livros'),

]
