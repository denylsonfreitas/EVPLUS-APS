from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def cadastro(request):
    exibir_sidebar = False
    if request.method == 'GET':
        return render(request, 'cadastro.html', {'exibir_sidebar': exibir_sidebar})
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Verifica se o usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return render(request, 'cadastro.html', {'exibir_sidebar': exibir_sidebar, 'username': username, 'email': email})

        # Verifica se as senhas coincidem
        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem!')
            return render(request, 'cadastro.html', {'exibir_sidebar': exibir_sidebar, 'username': username, 'email': email})

        # Cria o usuário
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        return render(request, 'login.html', {'exibir_sidebar': exibir_sidebar})

@login_required
def home(request):
    exibir_sidebar = False
    return render(request, 'home.html', {'exibir_sidebar': exibir_sidebar})

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
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
            return render(request, 'login.html', {'exibir_sidebar': exibir_sidebar, 'error_message': 'Usuário ou senha inválidos!'})
        
@login_required
def home(request):
    exibir_sidebar = False
    return render(request, 'home.html', {'exibir_sidebar': exibir_sidebar})
