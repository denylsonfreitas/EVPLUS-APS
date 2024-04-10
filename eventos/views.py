#views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

@permission_required('eventos.add_evento', login_url='/auth/login/')
def eventos(request):
    exibir_sidebar = True
    if request.method == 'GET':
        eventos = Evento.objects.filter(user=request.user)
        return render(request, 'criarEvento.html', {'eventos': eventos, 'exibir_sidebar': exibir_sidebar})
    elif request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.user = request.user
            evento.save()
            return redirect('eventos:meuseventos')
        else:
            return render(request, 'criarEvento.html', {'form': form, 'exibir_sidebar': exibir_sidebar})
        
@login_required
@permission_required('eventos.add_evento', raise_exception=True)
def listarEventos(request):
    exibir_sidebar = True
    eventos = Evento.objects.filter(user=request.user)
    return render(request, 'meusEventos.html', {'eventos': eventos, 'exibir_sidebar': exibir_sidebar})

@permission_required('eventos.delete_evento', login_url='/auth/login/')
def cancelarEvento(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect('eventos:meuseventos')

@permission_required('eventos.change_evento', login_url='/auth/login/')
def editarEvento(request, id):
    exibir_sidebar = True
    try:
        evento = Evento.objects.get(id=id, user=request.user)
    except Evento.DoesNotExist:
        evento = None
    
    if evento:
        if request.method == 'GET':
            form = EventoForm(instance=evento)
            return render(request, 'editarEvento.html', {'form': form, 'exibir_sidebar': exibir_sidebar, 'evento': evento})
        elif request.method == 'POST':
            form = EventoForm(request.POST, request.FILES, instance=evento)
            if form.is_valid():
                form.save()
                return redirect('eventos:meuseventos')
            else:
                return render(request, 'editarEvento.html', {'form': form, 'exibir_sidebar': exibir_sidebar, 'evento': evento})
    else:
        return HttpResponse("O evento não foi encontrado.", status=404)

def detalhesEvento(request, id):
    exibir_sidebar = True
    evento = Evento.objects.get(id=id)
    usuario = request.user
    ja_inscrito = evento.clients.filter(pk=usuario.pk).exists()
    return render(request, 'visualizarEvento.html', {'evento': evento, 'exibir_sidebar': exibir_sidebar})

def listarTodosEventos(request):
    exibir_sidebar = True
    categoria = request.GET.get('categoria')
    if categoria:
        eventosDisponiveis = Evento.objects.filter(category=categoria)
    else:
        eventosDisponiveis = Evento.objects.all()
    return render(request, 'todosEventos.html', {'eventos': eventosDisponiveis, 'exibir_sidebar': exibir_sidebar})

@login_required
@permission_required('eventos.view_evento', raise_exception=True)
def listarEventosInscritos(request):
    exibir_sidebar = True
    eventos_inscritos = Evento.objects.filter(clients=request.user)
    return render(request, 'minhasInscricoes.html', {'eventos': eventos_inscritos, 'exibir_sidebar': exibir_sidebar})

@permission_required('eventos.view_evento', login_url='/auth/login/')
def inscricaoEvento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.user not in evento.clients.all():
        evento.clients.add(request.user)
        evento.save()
        return redirect('eventos:minhasinscricoes')
    else:
        return redirect('eventos:detalhes_evento', id=evento_id)

@permission_required('eventos.view_evento', login_url='/auth/login/')   
def cancelarInscricao(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.user in evento.clients.all():
        evento.clients.remove(request.user)
    return redirect('eventos:minhasinscricoes')

@permission_required('eventos.view_certificado', login_url='/auth/login/')
def listarCertificados(request, id):
    evento = Evento.objects.get(id=id)
    return render(request, 'certificado.html', {'evento': evento})