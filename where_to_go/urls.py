from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from places import views

urlpatterns = [
    url(
        r"^media/(?P<path>.*)$",
        serve,
        {"document_root": settings.MEDIA_ROOT},
    ),
    url(
        r"^static/(?P<path>.*)$",
        serve,
        {"document_root": settings.STATIC_ROOT},
    ),
    path("admin/", admin.site.urls),
    path("", views.index),
    path(
        "places/<int:pk>/",
        views.get_infо_location,
        name="info_location"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
