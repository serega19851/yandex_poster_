from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название места', max_length=200)
    place_id = models.CharField(
        'Уникальный идентификатор',
        max_length=50,
        null=True,
        unique=True
    )
    description_short = models.TextField('Короткое описание')
    description_long = HTMLField('Длинное описание')
    lng = models.FloatField('Долгота', null=True)
    lat = models.FloatField('Широта', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Места'
        verbose_name = 'Место'


class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        verbose_name='Относится к месту',
        related_name='images',
        on_delete=models.SET_NULL,
        null=True
    )
    img = models.ImageField('Картинка', upload_to='', null=True, blank=True)
    imagetitle = models.CharField(
        'Название изображения',
        max_length=70,
        null=True,
        unique=True,
    )
    my_order = models.PositiveIntegerField('Порядок', default=1)

    def __str__(self):
        return f'{self.pk} {self.place}'

    class Meta:
        verbose_name_plural = 'Картинки'
        verbose_name = 'Картинка'
        ordering = ['my_order']
