# Generated by Django 5.2.1 on 2025-06-20 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_alter_artigo_localizacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='localizacao',
            field=models.CharField(choices=[('Faro', 'Faro'), ('Quarteira', 'Quarteira'), ('Lagos', 'Lagos'), ('Lagoa', 'Lagoa'), ('Portimão', 'Portimão'), ('Albufeira', 'Albufeira'), ('Sagres', 'Sagres'), ('Aljez', 'Aljez'), ('Via Real de Santo António', 'Via Real de Santo António'), ('Olhão', 'Olhão'), ('Aljezur', 'Aljezur'), ('S. Teotónio', 'S. Teotónio'), ('Aljez', 'Aljez'), ('Ferreiras', 'Ferreiras'), ('Vidigueira', 'Vidigueira'), ('Barreira', 'Barreiro')], max_length=100),
        ),
    ]
