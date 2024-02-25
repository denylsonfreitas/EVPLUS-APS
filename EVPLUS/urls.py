from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('cadastro/', include('cadastro.urls')),
    path('home/', include('home.urls')),
    path('eventos/', include('eventos.urls')),
    path('conta/', include('conta.urls')),
    path('conta/meuseventos/', include('meuseventos.urls')),
    path('conta/certificado/', include('certificado.urls')),
]
