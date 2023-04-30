import json
import os
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Place


def index(request):
    places = Place.objects.all()
    context = {
        'saved_places': {
            "type": "FeatureCollection",
            "features": [

            ]
        }
    }
    for num, place in enumerate(places):
        detailsurl = ['../static/roofs24.json', '../static/moscow_legends.json']
        context['saved_places']['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                      "title": place.title,
                      "placeId": place.id,
                      "detailsUrl": f"{detailsurl[num]}"
                }
            }
        )
    return render(request, "index.html", context=context)


def gets_object_id(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_imgs = place.images.all()
    img_paths = [os.path.join('media', f'{image.img}') for image in place_imgs]
    context = {
        "title": place.title,
        "imgs": img_paths,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }
    return HttpResponse(
        json.dumps(context, ensure_ascii=False, indent=4),
        content_type="application/json"
    )
