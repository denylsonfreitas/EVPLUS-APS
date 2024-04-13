#models.py

from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clients = models.ManyToManyField(User, through='Inscricao', related_name='eventos')
    name = models.CharField(max_length=100)
    description = models.TextField()
    local = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    category = models.CharField(max_length=100)
    banner = models.ImageField(null=True, blank=True, upload_to='images/')
    limite_inscricoes = models.PositiveIntegerField(null=True, blank=True, verbose_name="Limite de Inscrições")
    finalizado = models.BooleanField(default=False)
    certificados = models.ManyToManyField(User, through='Certificado', related_name='eventos_certificados')

    def __str__(self):
        return self.name
    
class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['evento', 'user']

from django.db import models

class Certificado(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    participante = models.ForeignKey(User, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='certificados/')

    def __str__(self):
        return f"Certificado de {self.participante.username} para {self.evento.name}"
