from django.db import models
from django.core.exceptions import ValidationError

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class Cadastro(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100, default='')
    
    def clean(self):
        if self.password != self.confirm_password:
            raise ValidationError("A senha e a confirmação de senha não são iguais.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username
