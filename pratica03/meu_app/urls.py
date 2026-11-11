from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name = 'index'),
    path('cadastrar_livro/', views.cadastrar_livro, name = 'cadastrar_livro'),
    path('cadastrar_cliente/', views.cadastrar_cliente, name = 'cadastrar_cliente'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name = 'cadastrar_usuario'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
]
