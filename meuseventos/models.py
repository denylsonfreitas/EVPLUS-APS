from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    horario = models.TimeField()
    arquivo = models.FileField(upload_to='eventos/')

    def __str__(self):
        return self.nome
