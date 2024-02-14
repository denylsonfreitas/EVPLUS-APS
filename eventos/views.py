from django.shortcuts import render
from django.http import HttpResponse

def eventos(request):
    return render(request, 'eventos.html')
