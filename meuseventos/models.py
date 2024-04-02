from django.db import models
from eventos.models import Evento as EventoBase

class Evento(EventoBase):
    class Meta:
        proxy = True

    def __str__(self) -> str:
        return self.nome
