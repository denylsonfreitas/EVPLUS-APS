from django.shortcuts import render
from eventos.models import Evento

def meuseventos(request):
    eventos = Evento.objects.filter(usuario=request.user)
    return render(request, 'meuseventos.html', {'eventos': eventos})
