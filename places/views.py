from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Place


def index(request):
    places = Place.objects.all()
    features = []

    for place in places:
        features.append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat]
                },
                'properties': {
                      'title': place.title,
                      'placeId': place.id,
                      'detailsUrl': reverse('info_location', args=[place.id])
                }
            }
        )

    context = {
        'saved_places': {
            'type': 'FeatureCollection',
            'features': features
        }
    }
    return render(request, 'index.html', context=context)


def get_info_location(request, pk):
    place = get_object_or_404(Place, id=pk)
    place_imgs = place.images.all()
    img_paths = [image.img.url for image in place_imgs]
    context = {
        'title': place.title,
        'imgs': img_paths,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return JsonResponse(
        context,
        json_dumps_params={'ensure_ascii': False, 'indent': 4}
    )
