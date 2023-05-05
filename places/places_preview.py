from django.utils.html import format_html


def get_preview_places(image):
    return format_html(
        '<img src="{url}" height="{height}" />',
        url=image.img.url,
        height='200px',
    )
