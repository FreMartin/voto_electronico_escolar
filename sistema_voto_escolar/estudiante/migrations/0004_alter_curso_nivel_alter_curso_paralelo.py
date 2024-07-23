# Generated by Django 5.0.6 on 2024-07-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0003_alter_curso_nivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('Primero', 1), ('Segundo', 2), ('Tercero', 3), ('Cuarto', 4), ('Quinto', 5), ('Sexto', 6)], default='1', max_length=10),
        ),
        migrations.AlterField(
            model_name='curso',
            name='paralelo',
            field=models.CharField(choices=[('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd'), ('E', 'e'), ('F', 'f')], default='a', max_length=1),
        ),
    ]
