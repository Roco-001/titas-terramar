# Generated by Django 2.1 on 2020-09-12 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_product_visor'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url_media',
            field=models.URLField(blank=True, null=True, verbose_name='Enlace del Tutorial'),
        ),
    ]
