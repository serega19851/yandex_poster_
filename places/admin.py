from django.contrib import admin
from django.contrib.admin import TabularInline
from django.utils.html import format_html
from .models import Place, Image


class ImageAdminInline(TabularInline):
    extra = 1
    model = Image
    readonly_fields = ['headshot_image']
    fields = ('img', 'headshot_image',)

    def headshot_image(self, obj):
        return format_html(
            '<img src="{url}" style="max-height: 200px;"/>'.format(
                url=obj.img.url,
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = (ImageAdminInline,)
    list_display = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
