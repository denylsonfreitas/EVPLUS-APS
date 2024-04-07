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
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        date = request.POST.get('date')

        conta = Conta(
            name=name,
            email=email,
            password=password,
            phone=phone,
            date=date
        )

        conta.save()

        return redirect('home')

@login_required(login_url='/auth/login/')
def certificado(request):
    return render(request, 'certificado.html', {'exibir_sidebar': True})

@login_required(login_url='/auth/login/')
def meuseventos(request):
    return render(request, 'meuseventos.html', {'exibir_sidebar': True})
