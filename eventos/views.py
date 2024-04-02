from django.shortcuts import render
from .models import Evento

def eventos(request):
    exibir_sidebar = True
    if request.method == 'GET':
        return render(request, 'eventos.html', {'exibir_sidebar': exibir_sidebar})
    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        local = request.POST.get('local')
        date = request.POST.get('date')
        time = request.POST.get('time')
        category = request.POST.get('category')
        banner = request.FILES.get('banner')

        evento = Evento(
            name=name,
            description=description,
            local=local,
            date=date,
            time=time,
            category=category,
            banner=banner
        )

        evento.save()

        return render(request, 'meuseventos.html', {'exibir_sidebar': exibir_sidebar})