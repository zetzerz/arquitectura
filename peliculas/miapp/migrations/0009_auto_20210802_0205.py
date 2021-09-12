# Generated by Django 3.0 on 2021-08-02 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0008_auto_20210730_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='nombre_agenda',
            field=models.CharField(max_length=100, verbose_name='Nombre Contacto'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='proyecto_agenda',
            field=models.CharField(max_length=100, verbose_name='Nombre Proyecto'),
        ),
        migrations.AlterField(
            model_name='dato_cliente',
            name='detalle',
            field=models.CharField(blank=True, choices=[('ARQUITECTURA', 'ARQUITECTURA'), ('INGENIERIA', 'INGENIERIA'), ('TOPOGRAFIA', 'TOPOGRAFIA')], max_length=100, null=True),
        ),
    ]
