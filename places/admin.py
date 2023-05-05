from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin
from places.places_preview import get_preview_places


class ImageInline(SortableInlineAdminMixin, TabularInline):
    extra = 1
    model = Image
    raw_id_fields = ('place',)
    readonly_fields = [get_preview_places, ]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)
    list_display = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = [get_preview_places, ]
