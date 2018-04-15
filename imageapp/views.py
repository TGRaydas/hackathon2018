from django.shortcuts import render
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from django.template import loader


# Create your views here.
from django.http import HttpResponse


def index(request):
    template = loader.get_template('imageapp/index.html')
    return HttpResponse(template.render({}, request))