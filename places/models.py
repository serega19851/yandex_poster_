from django.db import models


class Place(models.Model):
    title = models.CharField('Название места', max_length=200)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Длинное описание')
    lng = models.DecimalField('Долгота', max_digits=16, decimal_places=14, null=True)
    lat = models.DecimalField('Широта', max_digits=16, decimal_places=14, null=True)

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
        null=True)
    img = models.ImageField('Картинка', upload_to='images', null=True, blank=True)

    def __str__(self):
        return f'{self.pk} {self.place}'

    class Meta:
        verbose_name_plural = 'Картинки'
        verbose_name = 'Картинка'
