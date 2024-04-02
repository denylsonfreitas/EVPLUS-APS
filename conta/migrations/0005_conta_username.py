# Generated by Django 4.2.3 on 2024-04-02 01:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0004_remove_conta_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, unique=True),
        ),
    ]
