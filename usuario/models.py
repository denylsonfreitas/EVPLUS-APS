from django.db import models
from django.core.exceptions import ValidationError

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class Cadastro(models.Model):
    name = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, default='')
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username
