from django.shortcuts import render
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from django.template import loader


# Create your views here.
from django.http import HttpResponse


def index(request):

    app = ClarifaiApp(api_key='f0e9f06f4bab4b0f918522fac94b2eb4')

    model = app.models.get('general-v1.3')
    # image = ClImage(url='https://samples.clarifai.com/metro-north.jpg')
    ls = []
    image = ClImage(url='https://samples.clarifai.com/metro-north.jpg')
    res = model.predict([image])

    hc_elements = hashtag_creator(res)
    hashtag_list = hc_elements[0]
    hashtag_str = hc_elements[1]

    print(res)
    context = {
        'hashtag_list': hashtag_list,
        'hashtag_str': hashtag_str
    }

    template = loader.get_template('imageapp/index.html')

    return HttpResponse(template.render(context, request))


'''def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ExampleModel.objects.get(pk=course_id)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')'''

def hashtag_creator(clarifai_response):
    hashtag_dict_list = clarifai_response['outputs'][0]['data']['concepts']
    hashtag_list = list()
    hashtag_string = ''

    for i in range(0, len(hashtag_dict_list)):
        if hashtag_dict_list[i]['name'] != 'no person':
            hashtag_list.append('#' + hashtag_dict_list[i]['name'])
            hashtag_string += '#' + hashtag_dict_list[i]['name']

    return [hashtag_list, hashtag_string]