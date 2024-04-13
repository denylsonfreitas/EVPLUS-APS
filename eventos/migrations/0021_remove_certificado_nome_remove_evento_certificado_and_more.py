# Generated by Django 4.2.3 on 2024-04-13 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0020_certificado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificado',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='certificado',
        ),
        migrations.AddField(
            model_name='certificado',
            name='evento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eventos.evento'),
        ),
        migrations.AddField(
            model_name='certificado',
            name='participante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
