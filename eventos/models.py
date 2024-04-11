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
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certificado = models.FileField(upload_to='certificados/', null=True, blank=True)

    class Meta:
        unique_together = ['evento', 'user']
