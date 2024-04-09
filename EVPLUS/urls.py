from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('auth/', include('usuario.urls')),
    path('eventos/', include('eventos.urls')),
    path('conta/', include('conta.urls')),
]
