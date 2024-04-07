from django.db import models
from django.utils import timezone

class Conta(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.username