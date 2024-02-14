from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    local = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    categoria = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='eventos', null=True, blank=True)

    def __str__(self) -> str:
        return self.nome
