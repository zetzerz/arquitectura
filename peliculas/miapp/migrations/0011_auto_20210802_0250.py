# Generated by Django 3.0 on 2021-08-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0010_auto_20210802_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dato_cliente',
            name='detalle',
            field=models.CharField(blank=True, choices=[('ARQUITECTURA', 'ARQUITECTURA'), ('INGENIERIA', 'INGENIERIA'), ('TOPOGRAFIA', 'TOPOGRAFIA'), ('ARQUITECTURA  INGENIERIA', 'ARQUITECTURA  INGENIERIA'), ('INGENIERIA  TOPOGRAFIA', 'INGENIERIA  TOPOGRAFIA'), ('ARQUITECTURA  TOPOGRAFIA', 'ARQUITECTURA  TOPOGRAFIA')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dato_cliente',
            name='pago_quinto',
            field=models.CharField(blank=True, default=0, max_length=100, null=True, verbose_name='PAGO INGENIRIA O TOPOGRAFIA'),
        ),
    ]
