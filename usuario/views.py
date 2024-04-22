from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes

def login(request):
    exibir_sidebar = True
    if request.method == 'GET':
        return render(request, 'login.html', {'exibir_sidebar': exibir_sidebar})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
            return render(request, 'login.html', {'exibir_sidebar': exibir_sidebar, 'username': username, 'error_message': 'Usuário ou senha inválidos!'})
        
def cadastro(request):
    exibir_sidebar = True
    if request.method == 'GET':
        return render(request, 'cadastro.html', {'exibir_sidebar': exibir_sidebar})
    elif request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return render(request, 'cadastro.html', {'exibir_sidebar': exibir_sidebar, 'username': username, 'email': email})

        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem!')
            return render(request, 'cadastro.html', {'exibir_sidebar': exibir_sidebar, 'username': username, 'email': email})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = name
        user.last_name = lastname
        user.save()
        
        return redirect('login')

def esqueceu_senha(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = request.build_absolute_uri('/') + 'resetar-senha/' + uid + '/' + token + '/'
            email_subject = 'Redefinir sua senha'
            email_body = render_to_string('resetar_senha_email.html', {
                'reset_url': reset_url,
            })
            email = EmailMessage(
                email_subject,
                email_body,
                'denyprime@gmail.com',
                [email],
            )
            email.send()
        return redirect('senha_enviada')
    return render(request, 'esqueceu_senha.html')

def senha_enviada(request):
    return render(request, 'senha_enviada.html')

@login_required
def home(request):
    exibir_sidebar = False
    return render(request, 'home.html', {'exibir_sidebar': exibir_sidebar})

@login_required
def meuseventos(request):
    exibir_sidebar = False
    return render(request, 'meusEventos.html', {'exibir_sidebar': exibir_sidebar})

@login_required
def certificado(request):
    exibir_sidebar = False
    return render(request, 'certificado.html', {'exibir_sidebar': exibir_sidebar})

@login_required
def eventos(request):
    exibir_sidebar = False
    return render(request, 'eventos.html', {'exibir_sidebar': exibir_sidebar})

@login_required
def conta(request):
    return redirect('login')
