from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Conta

@login_required(login_url='/auth/login/')
def conta(request):
    exibir_sidebar = True
    usuario = request.user
    if request.method == 'GET':
        return render(request, 'conta.html', {'exibir_sidebar': exibir_sidebar, 'usuario': usuario})
    elif request.method == 'POST':
        usuario.name = request.POST.get('name')
        usuario.username = request.POST.get('username')
        usuario.email = request.POST.get('email')
        usuario.password = request.POST.get('password')
        usuario.save()
        return redirect('home')

@login_required(login_url='/auth/login/')
def certificado(request):
    return render(request, 'certificado.html', {'exibir_sidebar': True})
