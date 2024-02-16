from django.db import models

class Conta(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date = models.DateField()
    
    def __str__(self) -> str:
        return self.nome
