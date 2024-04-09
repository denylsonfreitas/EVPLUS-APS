from django.shortcuts import render, redirect
from .models import Evento
from .forms import EventoForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login/')
def eventos(request):
    exibir_sidebar = True
    if request.method == 'GET':
        eventos = Evento.objects.filter(user=request.user)
        return render(request, 'eventos.html', {'eventos': eventos, 'exibir_sidebar': exibir_sidebar})
    elif request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.user = request.user
            evento.save()
            return redirect('meuseventos')
        else:
            return render(request, 'eventos.html', {'form': form, 'exibir_sidebar': exibir_sidebar})
        
@login_required(login_url='/auth/login/')
def listarEventos(request):
    exibir_sidebar = True
    eventos = Evento.objects.filter(user=request.user)
    return render(request, 'meuseventos.html', {'eventos': eventos, 'exibir_sidebar': exibir_sidebar})

@login_required(login_url='/auth/login/')
def deletarEvento(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect('meuseventos')

@login_required(login_url='/auth/login/')
def editarEvento(request, id):
    evento = Evento.objects.get(id=id)
    if request.method == 'GET':
        form = EventoForm(instance=evento)
        return render(request, 'editar_evento.html', {'form': form})
    elif request.method == 'POST':
        form = EventoForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('meuseventos')
        else:
            return render(request, 'editar_evento.html', {'form': form})
        
@login_required(login_url='/auth/login/')
def detalhesEvento(request, id):
    evento = Evento.objects.get(id=id)
    return render(request, 'detalhes_evento.html', {'evento': evento})

@login_required(login_url='/auth/login/')
def inscricaoEvento(request, id):
    evento = Evento.objects.get(id=id)
    return render(request, 'inscricao_evento.html', {'evento': evento})

@login_required(login_url='/auth/login/')
def listarCertificados(request, id):
    evento = Evento.objects.get(id=id)
    return render(request, 'certificado.html', {'evento': evento})

@login_required(login_url='/auth/login/')
def gerarCertificado(request, id):
    evento = Evento.objects.get(id=id)
    return render(request, 'gerar_certificado.html', {'evento': evento})