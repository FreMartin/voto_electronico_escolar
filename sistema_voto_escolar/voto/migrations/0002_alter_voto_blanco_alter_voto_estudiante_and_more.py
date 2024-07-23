# Generated by Django 5.0.6 on 2024-07-07 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0004_alter_curso_nivel_alter_curso_paralelo'),
        ('lista', '0001_initial'),
        ('voto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voto',
            name='blanco',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voto',
            name='estudiante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='estudiante.estudiante'),
        ),
        migrations.AlterField(
            model_name='voto',
            name='lista',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lista.lista'),
        ),
        migrations.AlterField(
            model_name='voto',
            name='nulo',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
