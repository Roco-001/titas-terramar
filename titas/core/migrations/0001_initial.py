# Generated by Django 2.1 on 2020-08-27 01:40

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categoría',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('titular', ckeditor.fields.RichTextField(max_length=100, verbose_name='Titular')),
                ('descripcion', ckeditor.fields.RichTextField(verbose_name='Descripción')),
                ('precio', models.FloatField(default=100, verbose_name='Precio del Producto')),
                ('portada', models.ImageField(upload_to='portada', verbose_name='Adjunta la Imagen de la portada')),
                ('tipo_de_producto', models.CharField(max_length=50, verbose_name='Clave del Producto')),
                ('nuevo', models.BooleanField(blank=True, null=True, verbose_name='¿Producto es Nuevo?')),
                ('vistas_terramar', models.IntegerField(blank=True, null=True, verbose_name='Vistas Terramar')),
                ('ventas_terramar', models.IntegerField(blank=True, null=True, verbose_name='Ventas Terramar')),
                ('oferta', models.BooleanField(blank=True, null=True, verbose_name='¿Tiene alguna Oferta?')),
                ('precio_oferta', models.FloatField(blank=True, null=True, verbose_name='Precio de la Oferta')),
                ('descuento_oferta', models.IntegerField(blank=True, null=True, verbose_name='¿Porcentaje de la Oferta?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
            ],
            options={
                'verbose_name': 'SubCategoria',
                'verbose_name_plural': 'SubCategoria',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Subcategory'),
        ),
    ]
