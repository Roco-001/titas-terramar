# Generated by Django 2.1 on 2020-09-08 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_product_fisico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fisico',
            field=models.BooleanField(default=True, verbose_name='¿El producto es Físico?'),
        ),
    ]