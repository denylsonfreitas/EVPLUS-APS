from django.db import models

class Cadastro(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.username
