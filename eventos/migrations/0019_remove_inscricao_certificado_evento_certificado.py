# Generated by Django 4.2.3 on 2024-04-13 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0018_evento_limite_inscricoes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscricao',
            name='certificado',
        ),
        migrations.AddField(
            model_name='evento',
            name='certificado',
            field=models.FileField(blank=True, null=True, upload_to='certificados/'),
        ),
    ]
