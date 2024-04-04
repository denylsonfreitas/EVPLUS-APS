from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.conta, name='conta'),
    path('certificado/', views.certificado, name='certificado'),
    path('meuseventos/', views.meuseventos, name='meuseventos'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro')
]
