from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def gets_start_page(request):
    # template = loader.get_template('index.html')
    # context = {}
    # rendered_page = template.render(context, request)
    return render(request, 'index.html')
