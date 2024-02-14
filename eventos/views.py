from django.shortcuts import render
from django.http import HttpResponse

def eventos(request):
    if request.method == 'GET':
        return render(request, 'eventos.html')
    elif request.method == 'POST':
        nome = request.POST.get('name')
        descricao = request.POST.get('discription')
        local = request.POST.get('local')
        data = request.POST.get('date')
        hora = request.POST.get('time')
        categoria = request.POST.get('category')
        banner = request.FILES.get('banner')

        evento = Evento(
            nome=nome,
            descricao=descricao,
            local=local,
            data=data,
            hora=hora,
            categoria=categoria,
            banner=banner
        )

        evento.save()

        return HttpResponse('Evento cadastrado com sucesso!')
