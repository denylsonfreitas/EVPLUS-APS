from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

def cadastro(request):
    exibir_sidebar = False
    if request.method == 'GET':
        return render(request, 'cadastro.html', {'exibir_sidebar': exibir_sidebar})
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        user = User.objects.filter(username=username).first()
        if user:
            return HTTPResponse('Usuário já cadastrado!')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        return render(request, 'login.html', {'exibir_sidebar': exibir_sidebar})

def login(request):
    exibir_sidebar = False
    if request.method == 'GET':
        return render(request, 'login.html', {'exibir_sidebar': exibir_sidebar})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            auth_login(request, user)
            return HTTPResponse('Login realizado com sucesso!')
        else:
            return HTTPResponse('Usuário ou senha inválidos!')
        
@login_required
def home(request):
    exibir_sidebar = False
    return render(request, 'home.html', {'exibir_sidebar': exibir_sidebar})