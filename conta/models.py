from django.db import models
from django.utils import timezone

class Conta(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True, default='')
    email = models.EmailField()
    
    def __str__(self):
        return self.username