from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Conta

@login_required(login_url='/auth/login/')
def conta(request):
    exibir_sidebar = True
    if request.method == 'GET':
        return render(request, 'conta.html', {'exibir_sidebar': exibir_sidebar})
    elif request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        conta = Conta(
            name=name,
            username=username,
            email=email,
            password=password,
        )

        conta.save()

        return redirect('home')

@login_required(login_url='/auth/login/')
def certificado(request):
    return render(request, 'certificado.html', {'exibir_sidebar': True})
