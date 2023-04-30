from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import Place, Image


class ImageAdminInline(TabularInline):
    extra = 1
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = (ImageAdminInline,)
    list_display = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
