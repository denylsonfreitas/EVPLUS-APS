#views.py

from django.db.models import Avg
from .models import Evento, Certificado, Avaliacao
from .forms import EventoForm, CertificadoForm, AvaliacaoForm
from django.http import HttpResponse, FileResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

def erro(request):
    exibir_sidebar = True
    return render(request, 'erro.html', {'exibir_sidebar': exibir_sidebar})

@permission_required('eventos.add_evento', login_url='/auth/login/')
def eventos(request):

    if request.method == 'GET':
        eventos = Evento.objects.filter(user=request.user)
        return render(request, 'criarEvento.html', {'eventos': eventos})
    elif request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.user = request.user
            evento.save()
            return redirect('eventos:meuseventos')
        else:
            return render(request, 'criarEvento.html', {'form': form})
        
@login_required
@permission_required('eventos.add_evento', raise_exception=True)
def listarEventos(request):
    eventos_ativos = Evento.objects.filter(user=request.user, finalizado=False)
    eventos_finalizados = Evento.objects.filter(user=request.user, finalizado=True)
    return render(request, 'meusEventos.html', {'eventos': eventos_ativos, 'finalizarEvento': eventos_finalizados})

@permission_required('eventos.change_evento', login_url='/auth/login/')
def editarEvento(request, id):
    try:
        evento = Evento.objects.get(id=id, user=request.user)
    except Evento.DoesNotExist:
        evento = None
    
    if evento:
        if request.method == 'GET':
            form = EventoForm(instance=evento)
            return render(request, 'editarEvento.html', {'form': form, 'evento': evento})
        elif request.method == 'POST':
            form = EventoForm(request.POST, request.FILES, instance=evento)
            if form.is_valid():
                form.save()
                return redirect('eventos:meuseventos')
            else:
                return render(request, 'editarEvento.html', {'form': form, 'evento': evento})
    else:
        return render(request, 'erro.html')

def detalhesEvento(request, id):
    evento = get_object_or_404(Evento, id=id)
    comentarios = Avaliacao.objects.filter(evento=evento)
    media_notas = comentarios.aggregate(media=Avg('nota'))['media']
    
    if request.user.is_authenticated:
        avaliacao_usuario = Avaliacao.objects.filter(evento=evento, user=request.user).first()
    else:
        avaliacao_usuario = None
    
    permitir_avaliacao = True if not avaliacao_usuario else False
    
    return render(request, 'visualizarEvento.html', {'evento': evento, 'comentarios': comentarios, 'media_notas': media_notas})

def listarTodosEventos(request):
    categoria = request.GET.get('categoria')
    nome = request.GET.get('nome')
    
    eventosDisponiveis = Evento.objects.filter(finalizado=False) 
    
    if categoria:
        eventosDisponiveis = eventosDisponiveis.filter(category=categoria)
    if nome:
        eventosDisponiveis = eventosDisponiveis.filter(name__icontains=nome)
    
    for evento in eventosDisponiveis:
        if len(evento.name) > 15:
            evento.name = evento.name[:15] + '...'
        if len(evento.description) > 50:
            evento.description = evento.description[:50] + '...'
    
    return render(request, 'todosEventos.html', {'eventos': eventosDisponiveis})

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
def listarEventosInscritos(request):
    eventos = Evento.objects.filter(clients=request.user, finalizado=False)
    finalizarEvento = Evento.objects.filter(clients=request.user, finalizado=True)
    
    eventos_e_certificados = {}
    for evento in finalizarEvento:
        certificados = Certificado.objects.filter(evento=evento, participante=request.user)
        eventos_e_certificados[evento] = certificados
    
    return render(request, 'minhasInscricoes.html', {'eventos': eventos, 'finalizarEvento': finalizarEvento, 'eventos_e_certificados': eventos_e_certificados})

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

@login_required
@permission_required('eventos.add_evento', raise_exception=True)
def enviarCertificado(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)

    if request.method == 'POST':
        form = CertificadoForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = form.cleaned_data['arquivo']
            if request.POST.get('enviar_para_todos'):
                for participante in evento.clients.all():
                    certificado, created = Certificado.objects.get_or_create(evento=evento, participante=participante)
                    certificado.arquivo = arquivo
                    certificado.save()
            else:
                participante_id = request.POST.get('participante_selecionado')
                try:
                    participante = User.objects.get(pk=participante_id)
                    if participante in evento.clients.all():
                        certificado, created = Certificado.objects.get_or_create(evento=evento, participante=participante)
                        certificado.arquivo = arquivo
                        certificado.save()
                    else:
                        motivo_erro = "O participante selecionado não está inscrito no evento"
                        return render(request, 'erro.html', {'motivo_erro': motivo_erro})
                except User.DoesNotExist:
                    motivo_erro = "O participante selecionado não existe"
                    return render(request, 'erro.html',  {'motivo_erro': motivo_erro})

            return redirect('eventos:meuseventos')
    else:
        form = CertificadoForm()

    return render(request, 'enviarCertificado.html', {'form': form, 'evento': evento})

@login_required
@permission_required('eventos.view_evento', raise_exception=True)
def downloadCertificado(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)

    if request.user in evento.clients.all():
        certificados = Certificado.objects.filter(evento=evento, participante=request.user)
        
        if certificados.exists():
            certificado = certificados.first()
            return FileResponse(open(certificado.arquivo.path, 'rb'))
        else:
            motivo_erro = "O certificado não pertence ao usuário"
            return render(request, 'erro.html', {'motivo_erro': motivo_erro})
    else:
        motivo_erro = "O usuário não está inscrito no evento"
        return render(request, 'erro.html', {'motivo_erro': motivo_erro})

@login_required
@permission_required('eventos.view_evento', raise_exception=True)
def enviarAvaliacao(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    avaliacao_existente = Avaliacao.objects.filter(evento=evento, user=request.user).first()
    
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=avaliacao_existente)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.evento = evento
            avaliacao.user = request.user
            avaliacao.save()
            comentarios = evento.avaliacoes.all()
            return redirect('eventos:detalhes_evento', id=avaliacao.evento.id)
    else:
        form = AvaliacaoForm(instance=avaliacao_existente)
    
    comentarios = evento.avaliacoes.all() if evento.avaliacoes.exists() else []
    
    return redirect('eventos:detalhes_evento', id=avaliacao.evento.id)

@login_required
@permission_required('eventos.view_evento', login_url='/auth/login/')
def deletarAvaliacao(request, avaliacao_id):
    avaliacao = get_object_or_404(Avaliacao, id=avaliacao_id)
    if request.user == avaliacao.user:
        avaliacao.delete()
    return redirect('eventos:detalhes_evento', id=avaliacao.evento.id)