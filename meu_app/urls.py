from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_livro/', views.cadastrar_livro, name='cadastrar_livro'),
    path('listar_livros/', views.listar_livros, name='listar_livros'),
    path('devolver_livro/<int:id>', views.devolver_livro, name='devolver_livro'),
    path('emprestar_livro/<int:id>', views.emprestar_livro, name='emprestar_livro'),
    path('desativar_livro/<int:id>/',views.desativar_livro, name='desativar_livro'),
    path('ativar_livro/<int:id>/', views.ativar_livro, name='ativar_livro'),
    path('editar_livro/<int:id>/', views.editar_livro, name='editar_livro'),
    path('excluir_livro/<int:id>/', views.excluir_livro, name='excluir_livro'),
    path('livros_inativos/', views.livros_inativos, name='livros_inativos'),
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario')
]
