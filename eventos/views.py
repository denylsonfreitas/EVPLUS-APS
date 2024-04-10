from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm
from django.contrib.auth.decorators import permission_required

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
        
@permission_required('eventos.view_evento', login_url='/auth/login/')
def listarEventos(request):
    exibir_sidebar = True
    eventos = Evento.objects.filter(user=request.user)
    return render(request, 'meusEventos.html', {'eventos': eventos, 'exibir_sidebar': exibir_sidebar})

@permission_required('eventos.delete_evento', login_url='/auth/login/')
def deletarEvento(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect('eventos:meuseventos')

@permission_required('eventos.change_evento', login_url='/auth/login/')
def editarEvento(request, id):
    exibir_sidebar = True
    evento = Evento.objects.get(id=id)
    if request.method == 'GET':
        form = EventoForm(instance=evento)
        return render(request, 'criarEvento.html', {'form': form, 'exibir_sidebar': exibir_sidebar})
    elif request.method == 'POST':
        form = EventoForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('eventos:meuseventos')
        else:
            return render(request, 'criarEvento.html', {'form': form, 'exibir_sidebar': exibir_sidebar})
        
@permission_required('eventos.view_evento', login_url='/auth/login/')
def detalhesEvento(request, id):
    exibir_sidebar = True
    evento = Evento.objects.get(id=id)
    return render(request, 'visualizarEvento.html', {'evento': evento, 'exibir_sidebar': exibir_sidebar})

def listarTodosEventos(request):
    exibir_sidebar = True
    eventosDisponiveis = Evento.objects.all()
    return render(request, 'todosEventos.html', {'eventos': eventosDisponiveis, 'exibir_sidebar': exibir_sidebar})

@permission_required('eventos.view_evento', login_url='/auth/login/')
def inscricaoEvento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.user not in evento.participantes.all():
        evento.participantes.add(request.user)
        evento.save()
        return redirect('detalhes_evento', id=evento_id)
    else:
        return redirect('detalhes_evento', id=evento_id)

@permission_required('eventos.view_certificado', login_url='/auth/login/')
def listarCertificados(request, id):
    evento = Evento.objects.get(id=id)
    return render(request, 'certificado.html', {'evento': evento})