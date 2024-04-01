from django.db import models

class Certificado(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    arquivo = models.FileField(upload_to='certificados/')

    def __str__(self):
        return self.nome
    
