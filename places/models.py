from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название места', max_length=200)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = HTMLField('Длинное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    class Meta:
        verbose_name_plural = 'Места'
        verbose_name = 'Место'

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        verbose_name='Относится к месту',
        related_name='images',
        on_delete=models.SET_NULL,
        null=True
    )
    img = models.ImageField(
        'Картинка',
        upload_to='',
        null=True,
        blank=True
    )
    imagetitle = models.CharField(
        'Название изображения',
        max_length=70,
        null=True,
        unique=True,
    )
    my_order = models.PositiveIntegerField('Порядок', default=1)

    class Meta:
        verbose_name_plural = 'Картинки'
        verbose_name = 'Картинка'
        ordering = ['my_order']

    def __str__(self):
        return f'{self.pk} {self.place}'
