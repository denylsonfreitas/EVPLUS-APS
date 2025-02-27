# Generated by Django 4.2.3 on 2024-04-19 13:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0025_avaliacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='avaliacoes',
            field=models.ManyToManyField(related_name='eventos_avaliados', through='eventos.Avaliacao', to=settings.AUTH_USER_MODEL),
        ),
    ]
