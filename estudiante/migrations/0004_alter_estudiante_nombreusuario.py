# Generated by Django 3.2.7 on 2021-12-09 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estudiante', '0003_auto_20211202_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='nombreUsuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Nombre del estudiante'),
        ),
    ]
