from hashlib import md5

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import requests
from places.models import Place, Image


class Command(BaseCommand):
    help = '''
    Загружает данные в БД по переданной ссылке,
    ссылка должна содержать json-файл.
    '''

    def add_arguments(self, parser):
        parser.add_argument('link', type=str, help='Ссылка на json-файл.')

    def download_place_images(self, place, images_links):
        for image_link in images_links:
            try:
                response = requests.get(image_link)
                response.raise_for_status()

                content_img = ContentFile(
                    response.content,
                    name=md5(response.content).hexdigest(),
                )
                Image.objects.create(place=place, img=content_img)
            except requests.exceptions.HTTPError as http_er:
                self.stderr.write(self.style.ERROR(
                    f'\n Ошибка загрузки изображения\n{http_er}\n\n'
                ))
                continue

    def handle(self, *args, **options):
        link = options.get('link')
        try:
            response = requests.get(link)
            response.raise_for_status()
            payload = response.json()
            images_links = payload.get('imgs', [])

            place, created = Place.objects.get_or_create(
                title=payload['title'],
                defaults={
                    'description_short': payload.get('description_short', ''),
                    'description_long': payload.get('description_long', ''),
                    'lng': payload.get('coordinates')['lng'],
                    'lat': payload.get('coordinates')['lat'],
                }
            )
            if not created:
                self.stdout.write(
                    self.style.WARNING(f'\n{place.title} уже есть в БД.\n')
                )
                return

        except requests.exceptions.HTTPError as http_error:
            self.stderr.write(self.style.ERROR(
                f'\n Ошибка загрузки json-файла.\n{http_error}\n\n'
            ))
            return
        except KeyError as key_error:
            self.stderr.write(self.style.ERROR(
                f'\n Отсутствует обязательный ключ\n{key_error}\n\n'
            ))
            return

        self.download_place_images(place, images_links)
        self.stdout.write(
            self.style.SUCCESS(f'\n{place.title} добавлено в БД.\n')
        )
