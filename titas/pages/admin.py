from django.contrib import admin

# Register your models here.
from .models import Page

class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Page, PageAdmin)