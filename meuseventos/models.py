from django.db import models

class Eventos(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    horario = models.TimeField()

    def __str__(self) -> str:
        return self.nome
