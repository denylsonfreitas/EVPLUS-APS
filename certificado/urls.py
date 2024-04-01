from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_certificados, name='lista_certificados'),
]

# Esta sendo chamado en conta/certificado/