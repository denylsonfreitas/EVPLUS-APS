from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('', views.eventos, name='eventos'),
    path('meuseventos/', views.listarEventos, name='meuseventos'),
    path('meuseventos/', views.listarEventosInscritos, name='meuseventos_inscritos'),
    path('detalhes/<int:id>/', views.detalhesEvento, name='detalhes_evento'),
    path('editar/<int:id>/', views.editarEvento, name='editar_evento'),
    path('deletar/<int:id>/', views.deletarEvento, name='deletar_evento'),
    path('todos-eventos/', views.listarTodosEventos, name='todos_eventos'),
    path('inscricao/<int:evento_id>/', views.inscricaoEvento, name='inscricao_evento'),
    path('remover-inscricao/<int:evento_id>/', views.removerInscricao, name='remover_inscricao'),
]
