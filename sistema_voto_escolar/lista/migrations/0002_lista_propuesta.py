# Generated by Django 5.0.6 on 2024-07-07 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista',
            name='propuesta',
            field=models.TextField(default='', max_length=500),
        ),
    ]
