# Generated by Django 4.2.3 on 2024-04-10 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0011_remove_conta_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta',
            name='lastname',
            field=models.CharField(default='', max_length=100),
        ),
    ]
