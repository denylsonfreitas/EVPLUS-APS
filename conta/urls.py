from django.urls import path
from . import views

urlpatterns = [
    path('', views.conta, name='conta'),
    path('certificado/', views.certificado, name='certificado'),
    path('meuseventos/', views.meuseventos, name='meuseventos'),
]