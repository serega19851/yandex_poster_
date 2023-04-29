# Generated by Django 3.2.18 on 2023-04-29 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название места')),
                ('description_short', models.TextField(verbose_name='Короткое описание')),
                ('description_long', models.TextField(verbose_name='Длинное описание')),
                ('lng', models.DecimalField(decimal_places=14, max_digits=16, null=True, verbose_name='Долгота')),
                ('lat', models.DecimalField(decimal_places=14, max_digits=16, null=True, verbose_name='Широта')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка')),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='places.place', verbose_name='Относится к месту')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
    ]
