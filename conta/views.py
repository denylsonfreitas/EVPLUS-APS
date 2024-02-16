from django.shortcuts import render

def conta(request):
    return render(request, 'conta.html')

def certificado(request):
    return render(request, 'certificado.html')

def meuseventos(request):
    return render(request, 'meuseventos.html')