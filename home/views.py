from django.shortcuts import render

def home(request):
    exibir_sidebar = True
    return render(request, 'home.html', {'exibir_sidebar': exibir_sidebar})