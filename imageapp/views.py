from django.shortcuts import render
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage


# Create your views here.
from django.http import HttpResponse


def index(request):
    app = ClarifaiApp(api_key='f0e9f06f4bab4b0f918522fac94b2eb4')

    model = app.models.get('general-v1.3')
    # image = ClImage(url='https://samples.clarifai.com/metro-north.jpg')
    ls = []
    image = ClImage(url='https://samples.clarifai.com/metro-north.jpg')
    res = model.predict([image])
    print(res)



    return HttpResponse(str(res))