# Generated by Django 5.0.6 on 2024-07-06 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0002_alter_curso_nivel_alter_curso_paralelo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('primero', 1), ('segundo', 2), ('tercero', 3), ('cuarto', 4), ('quinto', 5), ('sexto', 6)], default='1', max_length=10),
        ),
    ]
