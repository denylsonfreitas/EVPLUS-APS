from django.shortcuts import render

def cadastro(request):
    exibir_sidebar = False
    return render(request, 'cadastro.html', {'exibir_sidebar': exibir_sidebar})
