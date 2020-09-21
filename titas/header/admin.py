from django.contrib import admin
from .models import Header, Slider, Visor
# Register your models here.

class HeaderProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name',  'created' , 'updated')



admin.site.register(Header, HeaderProject)


class SliderProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name',  'created' , 'updated')

admin.site.register(Slider, SliderProject)


class VisorProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name',  'created' , 'updated')
    
admin.site.register(Visor, VisorProject)