import django
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0028_evento_avaliacoes'),  # Dependência da migração anterior
    ]

    operations = [
        migrations.CreateModel(
            name='Evento_Avaliacoes',  # Nome da tabela
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # Adicione os campos necessários aqui, como campos ForeignKey
                # Exemplo:
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Evento')),
                ('avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Avaliacao')),
            ],
        ),
    ]
