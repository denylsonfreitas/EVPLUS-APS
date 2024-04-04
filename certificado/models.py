from django.db import models

class Certificado(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='certificados/')

    def __str__(self):
        return self.name
    
