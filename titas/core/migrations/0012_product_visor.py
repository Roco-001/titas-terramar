# Generated by Django 2.1 on 2020-09-12 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0008_auto_20200911_1906'),
        ('core', '0011_subcategory_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='visor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='get_visor', to='header.Visor', verbose_name='Visor'),
        ),
    ]
