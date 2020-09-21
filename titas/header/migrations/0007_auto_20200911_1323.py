# Generated by Django 2.1 on 2020-09-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0006_auto_20200911_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='color_titulo1',
            field=models.CharField(blank=True, choices=[('#FFFFFF', 'Blaco'), ('#C0C0C0', 'Plateado'), ('#808080', 'Gris'), ('#000000', 'Negro'), ('#FF0000', 'Rojo'), ('#800000', 'Granada'), ('#FFFF00', 'Amarillo'), ('#808000', 'Oliva'), ('#00FF00', 'Lima'), ('#008000', 'Verde'), ('#00FFFF', 'Aqua'), ('#008080', 'Teal'), ('#0000FF', 'Azul'), ('#000080', 'Navy'), ('#FF00FF', 'Fucsia'), ('#800080', 'Purpura')], max_length=45, null=True, verbose_name='Selecciona Color del Titulo'),
        ),
        migrations.AddField(
            model_name='slider',
            name='color_titulo2',
            field=models.CharField(blank=True, choices=[('#FFFFFF', 'Blaco'), ('#C0C0C0', 'Plateado'), ('#808080', 'Gris'), ('#000000', 'Negro'), ('#FF0000', 'Rojo'), ('#800000', 'Granada'), ('#FFFF00', 'Amarillo'), ('#808000', 'Oliva'), ('#00FF00', 'Lima'), ('#008000', 'Verde'), ('#00FFFF', 'Aqua'), ('#008080', 'Teal'), ('#0000FF', 'Azul'), ('#000080', 'Navy'), ('#FF00FF', 'Fucsia'), ('#800080', 'Purpura')], max_length=45, null=True, verbose_name='Selecciona Color del Subtitulo'),
        ),
        migrations.AddField(
            model_name='slider',
            name='color_titulo3',
            field=models.CharField(blank=True, choices=[('#FFFFFF', 'Blaco'), ('#C0C0C0', 'Plateado'), ('#808080', 'Gris'), ('#000000', 'Negro'), ('#FF0000', 'Rojo'), ('#800000', 'Granada'), ('#FFFF00', 'Amarillo'), ('#808000', 'Oliva'), ('#00FF00', 'Lima'), ('#008000', 'Verde'), ('#00FFFF', 'Aqua'), ('#008080', 'Teal'), ('#0000FF', 'Azul'), ('#000080', 'Navy'), ('#FF00FF', 'Fucsia'), ('#800080', 'Purpura')], max_length=45, null=True, verbose_name='Selecciona Color del Subtitulo2'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='style_imagen_left',
            field=models.CharField(blank=True, help_text='Recuerda colocar el %', max_length=100, null=True, verbose_name='¿Desplazamiento de la Imagen a la Izquierda'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='style_imagen_rigth',
            field=models.CharField(blank=True, help_text='Recuerda colocar el %', max_length=100, null=True, verbose_name='¿Desplazamiento de la imagen a la Derecha'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='style_imagen_top',
            field=models.CharField(blank=True, help_text='Recuerda colocar el %', max_length=100, null=True, verbose_name='¿Desplazamiento de la imagen Vertical?'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='style_imagen_widgth',
            field=models.CharField(blank=True, help_text='Recuerda colocar el %', max_length=100, null=True, verbose_name='¿Tamaño de la imagen'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='style_text_left',
            field=models.CharField(blank=True, help_text='Recuerda colocar el %', max_length=100, null=True, verbose_name='¿Desplazamiento del texto a la Izquierda'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='style_text_rigth',
            field=models.CharField(blank=True, help_text='Recuerda colocar el %', max_length=100, null=True, verbose_name='¿Desplazamiento del texto a la Derecha'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='style_text_top',
            field=models.CharField(blank=True, help_text='Recuerda colocar el %', max_length=100, null=True, verbose_name='¿Desplazamiento del texto Vertical?'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='style_text_widgth',
            field=models.CharField(blank=True, help_text='Recuerda colocar el %', max_length=100, null=True, verbose_name='¿Tamaño del texto'),
        ),
    ]