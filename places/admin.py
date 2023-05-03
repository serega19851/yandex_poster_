from django.contrib import admin
from django.contrib.admin import TabularInline
from django.utils.html import format_html
from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, TabularInline):
    extra = 1
    model = Image
    raw_id_fields = ('place',)
    readonly_fields = ['headshot_image']

    def headshot_image(self, obj):
        return format_html(
            '<img src="{url}" height="{height}" />'.format(
                url=obj.img.url,
                height='200px',
                )
            )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)
    list_display = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['place_img', ]

    def place_img(self, obj):
        return format_html(
            '<img src="{url}" height="{height}" />'.format(
                url=obj.img.url,
                height='200px',
            )
        )
