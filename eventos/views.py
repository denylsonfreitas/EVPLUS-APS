from django.shortcuts import render
from .models import Evento

def eventos(request):
    exibir_sidebar = True
    if request.method == 'GET':
        return render(request, 'eventos.html', {'exibir_sidebar': exibir_sidebar})
    elif request.method == 'POST':
        name = request.POST.get('name')
        discription = request.POST.get('discription')
        local = request.POST.get('local')
        date = request.POST.get('date')
        time = request.POST.get('time')
        category = request.POST.get('category')
        banner = request.FILES.get('banner')

        evento = Evento(
            name=name,
            discription=discription,
            local=local,
            date=date,
            time=time,
            category=category,
            banner=banner
        )

        evento.save()

        return render(request, 'home.html')