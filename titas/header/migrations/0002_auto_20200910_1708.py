# Generated by Django 2.1 on 2020-09-10 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='header',
            options={'ordering': ['-created'], 'verbose_name': 'Banner', 'verbose_name_plural': 'Banner'},
        ),
        migrations.RemoveField(
            model_name='header',
            name='size',
        ),
        migrations.AddField(
            model_name='header',
            name='imagen_banner',
            field=models.ImageField(blank=True, null=True, upload_to='Banner', verbose_name='Adjunta la Imagen del Banner'),
        ),
        migrations.AddField(
            model_name='header',
            name='imagen_logo_banner',
            field=models.ImageField(blank=True, null=True, upload_to='Logo_Banner', verbose_name='¿Quieres Cambiar el Logo? '),
        ),
        migrations.AddField(
            model_name='header',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Nombre del Banner'),
        ),
        migrations.AddField(
            model_name='header',
            name='style_facebook',
            field=models.CharField(blank=True, choices=[('facebookBlanco', 'Blanco'), ('facebookNegro', 'Negro'), ('facebookColor', 'Color')], max_length=45, null=True, verbose_name='Color del Facebook?'),
        ),
        migrations.AddField(
            model_name='header',
            name='style_google',
            field=models.CharField(blank=True, choices=[('googleColor', 'Color'), ('googleBlanco', 'Blanco'), ('googleNegro', 'Negro')], max_length=45, null=True, verbose_name='Color del Youtube?'),
        ),
        migrations.AddField(
            model_name='header',
            name='style_instagram',
            field=models.CharField(blank=True, choices=[('instagramColor', 'Color'), ('instagramBlanco', 'Blanco'), ('instagramNegro', 'Negro')], max_length=45, null=True, verbose_name='Color del Youtube?'),
        ),
        migrations.AddField(
            model_name='header',
            name='style_tex_banner',
            field=models.CharField(blank=True, choices=[('textoDer', 'Derecha'), ('textoIzq', 'Izquierda'), ('textoCentro', 'Centrado')], max_length=45, null=True, verbose_name='Selecciona Ubicacion del Texto'),
        ),
        migrations.AddField(
            model_name='header',
            name='style_twitter',
            field=models.CharField(blank=True, choices=[('twitterColor', 'Color'), ('twitterBlanco', 'Blanco'), ('youtubeNegro', 'Negro')], max_length=45, null=True, verbose_name='Color del Twitter?'),
        ),
        migrations.AddField(
            model_name='header',
            name='style_youtube',
            field=models.CharField(blank=True, choices=[('youtubeColor', 'Color'), ('youtubeBlanco', 'Blanco'), ('youtubeNegro', 'Negro')], max_length=45, null=True, verbose_name='Color del Youtube?'),
        ),
        migrations.AddField(
            model_name='header',
            name='titulo1_banner',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Titulo del Banner'),
        ),
        migrations.AddField(
            model_name='header',
            name='titulo2_banner',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='SubTitulo del Banner'),
        ),
        migrations.AddField(
            model_name='header',
            name='titulo3_banner',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='SubTitulo2 del Banner'),
        ),
    ]
