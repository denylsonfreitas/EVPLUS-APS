#urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('', views.eventos, name='eventos'),
    path('meuseventos/', views.listarEventos, name='meuseventos'),
    path('minhasinscricoes/', views.listarEventosInscritos, name='minhasinscricoes'),
    path('detalhes/<int:id>/', views.detalhesEvento, name='detalhes_evento'),
    path('editar/<int:id>/', views.editarEvento, name='editar_evento'),
    path('cancelar/<int:id>/', views.cancelarEvento, name='cancelar_evento'),
    path('todos-eventos/', views.listarTodosEventos, name='todos_eventos'),
    path('inscricao/<int:evento_id>/', views.inscricaoEvento, name='inscricao_evento'),
    path('cancelar-inscricao/<int:evento_id>/', views.cancelarInscricao, name='cancelar_inscricao'),
    path('finalizar/<int:id>/', views.finalizarEvento, name='finalizar_evento'),
    path('apagar/<int:id>/', views.apagarEvento, name='apagar_evento'),
    path('enviar-certificado/<int:evento_id>/', views.enviarCertificado, name='enviar_certificado'),
    path('download-certificado/<int:evento_id>/', views.downloadCertificado, name='download_certificado'),
    path('erro/', views.erro, name='erro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
