from django.shortcuts import render
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
