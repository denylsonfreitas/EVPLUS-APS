from django.db import models

class Certificado(models.Model):
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.id
    
