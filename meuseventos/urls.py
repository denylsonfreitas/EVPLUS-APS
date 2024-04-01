from django.urls import path
from . import views

urlpatterns = [
    path('', views.meus_eventos, name='meus_eventos'),
]