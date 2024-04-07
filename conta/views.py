# views.py na aplicação 'conta'
from django.shortcuts import render, redirect
from .models import Conta

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
def certificado(request):
    return render(request, 'certificado.html', {'exibir_sidebar': True})

def meuseventos(request):
    return render(request, 'meuseventos.html', {'exibir_sidebar': True})
