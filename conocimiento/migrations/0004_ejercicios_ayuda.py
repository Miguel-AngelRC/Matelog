# Generated by Django 3.2.7 on 2021-12-18 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conocimiento', '0003_alter_temas_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejercicios',
            name='ayuda',
            field=models.TextField(default=2, max_length=1000, verbose_name='Ayuda'),
            preserve_default=False,
        ),
    ]
