from django.db import models
from colorfield.fields import ColorField

STYLES_TEX = (
            ('textoDer','Derecha'),
            ('textoIzq','Izquierda'),
            ('textoCentro','Centrado'),            
            )

STYLES_FACEBOOK = (
            ('facebookBlanco','Blanco'),
            ('facebookNegro','Negro'),
            ('facebookColor','Color'),            
            )

STYLES_YOUTUBE = (
            ('youtubeColor','Color'),
            ('youtubeBlanco','Blanco'),
            ('youtubeNegro','Negro'),            
            )

STYLES_TWITTER = (
            ('twitterColor','Color'),
            ('twitterBlanco','Blanco'),
            ('youtubeNegro','Negro'),            
            )


STYLES_GOOGLE = (
            ('googleColor','Color'),
            ('googleBlanco','Blanco'),
            ('googleNegro','Negro'),            
            )


STYLES_INSTAGRAM = (
            ('instagramColor','Color'),
            ('instagramBlanco','Blanco'),
            ('instagramNegro','Negro'),            
            )


STYLES_TEX_SLIDER = (
            ('slideOpcion1','Opción 1'),
            ('slideOpcion2','Opción 2'),                      
            )

STYLES_TEX_COLOR = (
            ('#FFFFFF','Blanco'),
            ('#C0C0C0','Plateado'),
            ('#808080','Gris'),
            ('#000000','Negro'),
            ('#FF0000','Rojo'),
            ('#800000','Granada'),                      
            ('#FFFF00','Amarillo'),
            ('#808000','Oliva'),
            ('#00FF00','Lima'),
            ('#008000','Verde'),
            ('#00FFFF','Aqua'),
            ('#008080','Teal'),
            ('#0000FF','Azul'),
            ('#000080','Navy'),
            ('#FF00FF','Fucsia'),
            ('#800080','Purpura'),
            )

# Create your models here.
class  Header(models.Model):
    #DESCRIPCION DETALLADA  DEL PRODUCTO  CAMPOS OBLIGATORIOS
    name = models.CharField(max_length=100,  verbose_name="Nombre del Banner", default = 'Campaña')
    titulo1_banner = models.CharField(max_length=100, blank= True, null= True, verbose_name="Titulo del Banner") 
    color_titulo1_banner = ColorField(verbose_name="Selecciona Color del Titulo", blank= True, null= True,  default = '#000000')
    titulo2_banner = models.CharField(max_length=100, blank= True, null= True, verbose_name="SubTitulo del Banner")
    color_titulo2_banner = ColorField(verbose_name="Selecciona Color del Titulo 2", blank= True, null= True,  default = '#000000')
    titulo3_banner = models.CharField(max_length=100, blank= True, null= True,  verbose_name="SubTitulo2 del Banner")
    color_titulo3_banner = ColorField(verbose_name="Selecciona Color del Titulo 3", blank= True, null= True,  default = '#000000')
    imagen_banner  = models.ImageField(blank= True, null= True, verbose_name= 'Adjunta la Imagen del Banner', upload_to = 'Banner')    
    imagen_logo_banner  = models.ImageField(blank= True, null= True, verbose_name= '¿Quieres Cambiar el Logo? ', upload_to = 'Logo_Banner')    
    style_tex_banner = models.CharField(choices=STYLES_TEX, max_length=45,  verbose_name="Selecciona Ubicacion del Texto", blank= True, null= True)
    style_facebook = models.CharField(choices=STYLES_FACEBOOK, max_length=45,  verbose_name="Color del Facebook?", blank= True, null= True)    
    style_youtube  = models.CharField(choices=STYLES_YOUTUBE, max_length=45,  verbose_name="Color del Youtube?", blank= True, null= True)
    style_twitter  = models.CharField(choices=STYLES_TWITTER, max_length=45,  verbose_name="Color del Twitter?", blank= True, null= True)
    style_google  = models.CharField(choices=STYLES_GOOGLE, max_length=45,  verbose_name="Color del Google?", blank= True, null= True)
    style_instagram = models.CharField(choices=STYLES_INSTAGRAM, max_length=45,  verbose_name="Color del Instagram?", blank= True, null= True)

    barrasuperior = ColorField(verbose_name="Selecciona Color de la barra Superior", blank= True, null= True,  default = '#000000')
    barrainferior = ColorField(verbose_name="Selecciona Color del Barra Inferior", blank= True, null= True, default = '#000000')
    textoinferior = ColorField(verbose_name="Selecciona Color del Texto Inferior", blank= True, null= True, default = '#333333')

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
      
    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
        #Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]

    def __str__(self):
        return self.name


class  Slider(models.Model):
    #DESCRIPCION DETALLADA  DEL PRODUCTO  CAMPOS OBLIGATORIOS
    
    name = models.CharField(max_length=100,  verbose_name="Nombre del Slider")
    imagen_fondo_slider  = models.ImageField(blank= True, null= True, verbose_name= 'Adjunta la Imagen del Fondo', upload_to = 'Slider Fondo')
    imagen_prodcuto_slider  = models.ImageField(blank= True, null= True, verbose_name= 'Adjunta la Imagen del Prodcuto', upload_to = 'Slider Producto')
    style_tex_slider = models.CharField(choices=STYLES_TEX_SLIDER, max_length=45,  verbose_name="Selecciona Ubicacion del Texto", blank= True, null= True, help_text = 'Opción 1: Imagen a la derecha y texto izquierda Opción 2: Imagen a la izquierda y texto derecha')
    
    #CONTENIDOS DEL SLIDER
    titulo1_slider = models.CharField(max_length=100, blank= True, null= True, verbose_name="Titulo del Slider")
    color_titulo1 = ColorField(verbose_name="Selecciona Color del Titulo", blank= True, null= True) 
    titulo2_slider = models.CharField(max_length=100, blank= True, null= True, verbose_name="SubTitulo del Slider")
    color_titulo2 =  ColorField(verbose_name="Selecciona Color del Subtitulo", blank= True, null= True) 
    titulo3_slider = models.CharField(max_length=100, blank= True, null= True,  verbose_name="SubTitulo2 del Slider")
    color_titulo3 =  ColorField(verbose_name="Selecciona Color del Subtitulo2", blank= True, null= True) 
    

    #ESTILOS DE LA IMAGEN
    style_imagen_top = models.CharField(max_length=100, blank= True, null= True,verbose_name= "Imagen Top?",help_text = 'Recuerda colocar el %')
    style_imagen_rigth = models.CharField(max_length=100, blank= True, null= True,verbose_name= "Imagen Rigth?",help_text = 'Recuerda colocar el %')
    style_imagen_left = models.CharField(max_length=100, blank= True, null= True,verbose_name= "Imagen Left?",help_text = 'Recuerda colocar el %')
    style_imagen_widgth = models.CharField(max_length=100, blank= True, null= True,verbose_name= "Imagen Widgth?",help_text = 'Recuerda colocar el %')

    #ESTILOS DEL CONTENIDO
    style_text_top = models.CharField(max_length=100, blank= True, null= True,verbose_name= "Texto Top?",help_text = 'Recuerda colocar el %')
    style_text_rigth = models.CharField(max_length=100, blank= True, null= True,verbose_name= "Texto Rigth?",help_text = 'Recuerda colocar el %')
    style_text_left = models.CharField(max_length=100, blank= True, null= True,verbose_name= "Texto Left?",help_text = 'Recuerda colocar el %')
    style_text_widgth =models.CharField(max_length=100, blank= True, null= True,verbose_name= "Texto Widgth?",help_text = 'Recuerda colocar el %')

   

    #BOTON DE VER MAS Y URLS
    boton = models.BooleanField(verbose_name= "¿Quieres colocar el boton?" , default = True) 
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    
    

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
      
    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"
        #Ordena de mas nuevo a mas antiguo
        ordering = ["created"]

    def __str__(self):
        return self.name



class  Visor(models.Model):
    #FOTOS DEL VISOR EN CASO DE TENERLAS SINO SE MOSTRARA LA FOTO 
    
    name = models.CharField(max_length=100,  verbose_name="Nombre del Producto")
    clave = models.CharField(max_length=100,  verbose_name="Clave del Producto")
    imagen1  = models.ImageField(blank= True, null= True, verbose_name= 'Adjunta Imagen Visor', upload_to = 'Visor')
    imagen2  = models.ImageField(blank= True, null= True, verbose_name= 'Adjunta Imagen Visor', upload_to = 'Visor')
    imagen3  = models.ImageField(blank= True, null= True, verbose_name= 'Adjunta Imagen Visor', upload_to = 'Visor')
    imagen4  = models.ImageField(blank= True, null= True, verbose_name= 'Adjunta Imagen Visor', upload_to = 'Visor')
    imagen5  = models.ImageField(blank= True, null= True, verbose_name= 'Adjunta Imagen Visor', upload_to = 'Visor')
    imagen6  = models.ImageField(blank= True, null= True, verbose_name= 'Adjunta Imagen Visor', upload_to = 'Visor')    

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
      
    class Meta:
        verbose_name = "Visor"
        verbose_name_plural = "Visors"
        #Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]

    def __str__(self):
        return self.name


