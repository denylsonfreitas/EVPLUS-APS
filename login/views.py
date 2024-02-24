from django.shortcuts import render

def login(request):
    exibir_sidebar = False
    return render(request, 'login.html', {'exibir_sidebar': exibir_sidebar})

