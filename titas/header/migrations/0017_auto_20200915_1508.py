# Generated by Django 2.1 on 2020-09-15 20:08

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0016_auto_20200913_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='color_titulo1_banner',
            field=colorfield.fields.ColorField(blank=True, default='#000000', max_length=18, null=True, verbose_name='Selecciona Color del Titulo'),
        ),
        migrations.AddField(
            model_name='header',
            name='color_titulo2_banner',
            field=colorfield.fields.ColorField(blank=True, default='#000000', max_length=18, null=True, verbose_name='Selecciona Color del Titulo 2'),
        ),
        migrations.AddField(
            model_name='header',
            name='color_titulo3_banner',
            field=colorfield.fields.ColorField(blank=True, default='#000000', max_length=18, null=True, verbose_name='Selecciona Color del Titulo 3'),
        ),
    ]