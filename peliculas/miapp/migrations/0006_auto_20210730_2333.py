# Generated by Django 3.0 on 2021-07-31 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0005_auto_20210730_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
