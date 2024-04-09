from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

@login_required(login_url='/auth/login/')
def conta(request):
    exibir_sidebar = True
    usuario = request.user
    
    if request.method == 'GET':
        return render(request, 'conta.html', {'exibir_sidebar': exibir_sidebar, 'usuario': usuario})
    
    elif request.method == 'POST':
        new_name = request.POST.get('name')
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        
        # Verifica se o novo nome de usuário já está cadastrado
        if new_username != usuario.username and User.objects.filter(username=new_username).exists():
            messages.error(request, 'O nome de usuário já está em uso. Escolha outro.')
            return render(request, 'conta.html', {'exibir_sidebar': exibir_sidebar, 'usuario': usuario})
        
        # Verifica se o novo email já está cadastrado
        if new_email != usuario.email and User.objects.filter(email=new_email).exists():
            messages.error(request, 'O email já está em uso. Escolha outro.')
            return render(request, 'conta.html', {'exibir_sidebar': exibir_sidebar, 'usuario': usuario})

        usuario.first_name = new_name
        usuario.username = new_username
        usuario.email = new_email
        usuario.save()
        
        messages.success(request, 'Alterações salvas com sucesso!')
        return  render(request, 'conta.html', {'exibir_sidebar': exibir_sidebar, 'usuario': usuario})

@login_required(login_url='/auth/login/')
def certificado(request):
    return render(request, 'certificado.html', {'exibir_sidebar': True})
