from django.db import models

class Eventos(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    time = models.TimeField()

    def __str__(self) -> str:
        return self.name
