from django.db import models

class Evento(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField()
    local = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    category = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='eventos', null=True, blank=True)

    def __str__(self) -> str:
        return self.nome
