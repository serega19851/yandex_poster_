from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.DecimalField(max_digits=16, decimal_places=14, null=True)
    lat = models.DecimalField(max_digits=16, decimal_places=14, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Места'
        verbose_name = 'Место'
