# Generated by Django 2.1 on 2020-09-12 18:40

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0011_auto_20200912_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='barrainferior',
            field=colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='Selecciona Color del Barra Inferior'),
        ),
        migrations.AlterField(
            model_name='header',
            name='barrasuperior',
            field=colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='Selecciona Color de la barra Superior'),
        ),
        migrations.AlterField(
            model_name='header',
            name='textoinferior',
            field=colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='Selecciona Color del Texto Inferior'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='color_titulo1',
            field=colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='Selecciona Color del Titulo'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='color_titulo2',
            field=colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='Selecciona Color del Subtitulo'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='color_titulo3',
            field=colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='Selecciona Color del Subtitulo2'),
        ),
    ]