# Generated by Django 3.0 on 2021-08-18 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0020_persona_lote_lote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona_lote',
            name='lote',
        ),
        migrations.DeleteModel(
            name='lote',
        ),
        migrations.DeleteModel(
            name='persona_lote',
        ),
    ]
