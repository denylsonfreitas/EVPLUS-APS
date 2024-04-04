from django.urls import path
from . import views

urlpatterns = [
    path('', views.certificado_list, name='certificado_list'),
]

# Esta sendo chamado en conta/certificado/