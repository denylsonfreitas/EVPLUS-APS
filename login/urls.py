from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
]

# Esta sendo chamado em login/urls.py