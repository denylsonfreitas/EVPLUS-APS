from django.shortcuts import render, redirect
from .models import Evento
from .forms import EventoForm

def eventos(request):
    exibir_sidebar = True
    if request.method == 'GET':
        eventos = Evento.objects.all()
        return render(request, 'eventos.html', {'eventos': eventos, 'exibir_sidebar': exibir_sidebar})
    elif request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('meuseventos')
        else:
            return render(request, 'eventos.html', {'form': form, 'exibir_sidebar': exibir_sidebar})
