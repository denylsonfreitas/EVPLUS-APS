from django.shortcuts import redirect, render
from .models import Conta

def conta(request):
    if request.method == 'GET':
        return render(request, 'conta.html')
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
    return render(request, 'certificado.html')

def meuseventos(request):
    return render(request, 'meuseventos.html')