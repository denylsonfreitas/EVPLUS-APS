from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'), 
    path('esqueceu-senha/', views.esqueceu_senha, name='esqueceu_senha'),
    path('senha-enviada/', views.senha_enviada, name='senha_enviada'),
]
