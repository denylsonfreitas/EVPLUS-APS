from django.shortcuts import render

def meus_eventos(request):
    return render(request, 'meuseventos/meus_eventos.html')
