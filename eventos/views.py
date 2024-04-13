#views.py

from .models import Evento, Certificado
from .forms import EventoForm, CertificadoForm
from django.http import HttpResponse, FileResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
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
    eventos_ativos = Evento.objects.filter(user=request.user, finalizado=False)  # Filtra eventos ativos
    eventos_finalizados = Evento.objects.filter(user=request.user, finalizado=True)  # Filtra eventos finalizados
    return render(request, 'meusEventos.html', {'eventos': eventos_ativos, 'finalizarEvento': eventos_finalizados, 'exibir_sidebar': exibir_sidebar})

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
    nome = request.GET.get('nome')
    
    eventosDisponiveis = Evento.objects.filter(finalizado=False) 
    
    if categoria:
        eventosDisponiveis = eventosDisponiveis.filter(category=categoria)
    if nome:
        eventosDisponiveis = eventosDisponiveis.filter(name__icontains=nome)
    
    return render(request, 'todosEventos.html', {'eventos': eventosDisponiveis, 'exibir_sidebar': exibir_sidebar})

@permission_required('eventos.delete_evento', login_url='/auth/login/')
def cancelarEvento(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect('eventos:meuseventos')

@permission_required('eventos.add_evento', login_url='/auth/login/')
def finalizarEvento(request, id):
    evento = Evento.objects.get(id=id)
    evento.finalizado = True
    evento.save()
    return redirect('eventos:meuseventos')

@login_required
@permission_required('eventos.view_evento', raise_exception=True)
def listarEventosInscritos(request):
    exibir_sidebar = True
    eventos = Evento.objects.filter(clients=request.user, finalizado=False)
    finalizarEvento = Evento.objects.filter(clients=request.user, finalizado=True)
    return render(request, 'minhasInscricoes.html', {'eventos': eventos, 'finalizarEvento': finalizarEvento, 'exibir_sidebar': exibir_sidebar})


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

@permission_required('eventos.delete_evento', login_url='/auth/login/')
def apagarEvento(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect('eventos:meuseventos')
    
from .forms import CertificadoForm

@login_required
def gerenciarCertificados(request):
    exibir_sidebar = True
    eventos_finalizados = Evento.objects.filter(user=request.user, finalizado=True)
    return render(request, 'gerenciarCertificados.html', {'eventos_finalizados': eventos_finalizados, 'exibir_sidebar': exibir_sidebar})

@login_required
@permission_required('eventos.add_evento', raise_exception=True)
def enviarCertificado(request, evento_id):
    exibir_sidebar = True
    evento = get_object_or_404(Evento, pk=evento_id)

    if request.method == 'POST':
        form = CertificadoForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = form.cleaned_data['arquivo']
            if request.POST.get('enviar_para_todos'):
                for participante in evento.clients.all():
                    Certificado.objects.create(evento=evento, participante=participante, arquivo=arquivo)
            else:
                participantes_selecionados = request.POST.getlist('participantes_selecionados')
                for participante_id in participantes_selecionados:
                    participante = get_object_or_404(User, pk=participante_id)
                    Certificado.objects.create(evento=evento, participante=participante, arquivo=arquivo)

            return redirect('eventos:gerenciar_certificados')
    else:
        form = CertificadoForm()

    return render(request, 'enviarCertificado.html', {'form': form, 'exibir_sidebar': exibir_sidebar, 'evento': evento})

@login_required
@permission_required('eventos.add_inscricao', raise_exception=True)
def downloadCertificado(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    certificados = Certificado.objects.filter(evento=evento)

    if certificados.exists():
        certificado = certificados.first()
        return FileResponse(open(certificado.arquivo.path, 'rb'))
    else:
        raise HttpResponse("Certificado não encontrado.", status=404)

