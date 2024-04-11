#forms.py

from django import forms
from .models import Evento
from .models import Inscricao

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        exclude = ['user', 'clients', 'finalizado']

class CertificadoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['certificado']
