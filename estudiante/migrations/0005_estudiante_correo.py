# Generated by Django 3.2.7 on 2021-12-24 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0004_alter_estudiante_nombreusuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='correo',
            field=models.EmailField(default=1, max_length=254, verbose_name='Correo eléctronico'),
            preserve_default=False,
        ),
    ]
