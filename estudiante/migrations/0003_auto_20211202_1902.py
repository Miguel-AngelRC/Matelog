# Generated by Django 3.2.7 on 2021-12-03 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0002_alter_ejemplosestudiados_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejemplosestudiados',
            name='tiempo',
            field=models.IntegerField(verbose_name='Tiempo en segundos'),
        ),
        migrations.AlterField(
            model_name='ejerciciosestudiados',
            name='fecha',
            field=models.DateTimeField(verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='ejerciciosestudiados',
            name='tiempo',
            field=models.IntegerField(verbose_name='Tiempo en segundos'),
        ),
    ]
