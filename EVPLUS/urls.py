from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('eventos/', include('eventos.urls')),
    path('conta/', include('conta.urls')),
    path('meuseventos/', include('meuseventos.urls')),
    path('certificado/', include('certificado.urls')),
]
