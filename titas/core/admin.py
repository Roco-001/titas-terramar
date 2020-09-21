from django.contrib import admin
from .models import Category, Subcategory, Product
# Register your models here.


# Register your models here.
class CategoryProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name',  'created' , 'updated')
#  


class SubcategoryProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'category', 'created' , 'updated')
   
#  



class ProductProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('titulo', 'precio', 'subcategory', 'tipo_de_producto',  'created')
    list_filter = ('precio','nuevo', 'vistas_terramar', 'tipo_de_producto','fisico')
    search_fields = ('titulo','descripcion', 'titular', 'tipo_de_producto')
    date_hierarchy = 'fin_oferta'
#  

admin.site.register(Category, CategoryProject)

admin.site.register(Subcategory, SubcategoryProject)

admin.site.register(Product, ProductProject)