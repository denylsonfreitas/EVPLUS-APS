# Generated by Django 4.2.3 on 2024-04-07 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_cadastro_confirm_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro',
            name='confirm_password',
        ),
    ]
