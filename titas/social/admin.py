from django.contrib import admin

# Register your models here.
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created')
    pass

admin.site.register(Link, LinkAdmin)    