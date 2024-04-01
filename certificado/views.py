from django.shortcuts import render
from .models import Certificado

def lista_certificados(request):
    certificados = Certificado.objects.all()
    return render(request, 'certificado/lista_certificados.html', {'certificados': certificados})