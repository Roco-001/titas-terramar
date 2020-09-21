from django.db import models
from ckeditor.fields import RichTextField
from header.models import Header, Visor

# Create your models here.


class Category(models.Model):
    
    name = models.CharField(max_length=100, verbose_name="Nombre")         
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categoría"   

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    #id_category = models.AutoField(primary_key= True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= "get_subcategorys", verbose_name= "Categoria")    
    banner = models.ForeignKey(Header, on_delete=models.SET_NULL, related_name= "get_banners", verbose_name= "Campaña", blank= True, null= True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "SubCategoria"
        verbose_name_plural = "SubCategoria"

    

    def __str__(self):
        return self.name




class  Product(models.Model):
    #DESCRIPCION DETALLADA  DEL PRODUCTO  CAMPOS OBLIGATORIOS   
    
    titulo = models.CharField(max_length=100, verbose_name= "Titulo" )
    titular = RichTextField(max_length=200, verbose_name= "Titular")
    descripcion = RichTextField(verbose_name= "Descripción")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name= "get_products", verbose_name= "Subcategoria")
    banner = models.ForeignKey(Header, on_delete=models.SET_NULL, related_name= "get_banner", verbose_name= "Campaña", blank= True, null= True)
    visor = models.ForeignKey(Visor, on_delete=models.SET_NULL, related_name= "get_visor", verbose_name= "Visor", blank= True, null= True)  
    fisico = models.BooleanField(verbose_name= "¿El producto es Físico?" , default = True)
    url_media = models.URLField(verbose_name="Enlace del Tutorial", max_length=200, null=True, blank=True) 
    precio = models.FloatField(verbose_name= "Precio del Producto", default = 100)
    portada  = models.ImageField(verbose_name= 'Adjunta la Imagen de la portada', upload_to = 'portada') 
    tipo_de_producto = models.CharField(max_length=50, verbose_name= "Clave del Producto")
    nuevo =  models.BooleanField(blank= True, null= True, verbose_name= "¿Producto es Nuevo?", default = True)
    
    #PARA ORDERNAR LA PORTADA
    vistas_terramar = models.IntegerField(blank= True, null= True, verbose_name= "Vistas Terramar")
    ventas_terramar = models.IntegerField(blank= True, null= True, verbose_name= "Ventas Terramar")
    
    #OFERTAS EN CASO DE EXISTIR 
    oferta_categoria = models.BooleanField(blank= True, null= True, verbose_name= "¿Tiene Oferta la Categoria?", default = False)
    oferta_subcategoria = models.BooleanField(blank= True, null= True, verbose_name= "¿Tiene Oferta  la SubCategoria?", default = False)
    oferta = models.BooleanField(blank= True, null= True, verbose_name= "¿Tiene alguna Oferta?", default = False)
    precio_oferta = models.FloatField(blank= True, null= True,verbose_name= "Precio de la Oferta")   
    descuento_oferta = models.IntegerField(blank= True, null= True,verbose_name= "¿Porcentaje de la Oferta?")
    imagen_oferta  = models.ImageField(blank= True, null= True, verbose_name= 'Adjunta la Imagen de la Oferta', upload_to = 'Ofertas de la Portada')    
    fin_oferta = models.DateTimeField(blank= True, null= True,verbose_name= "Fecha de Fin de la Oferta")

    #DIAS PROMEDIO DE ENTREGA
    entrega = models.CharField(max_length=100,blank= True, null= True,verbose_name= "¿Dias promedio de entrega?")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
      
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        #Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]


    def __str__(self):
        return self.titulo