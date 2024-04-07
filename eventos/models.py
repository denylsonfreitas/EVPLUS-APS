from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    local = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    category = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='eventos', null=True, blank=True)

    def __str__(self):
        return self.name
