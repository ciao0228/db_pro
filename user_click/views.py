from django.shortcuts import render
import matplotlib.pyplot as plt
from db_pro import settings
from django.http import *

# Create your views here.

index_img = 0


def index(request):
    return render(request, 'index.html', locals())


from django.db import models


class Images(models.Model):
    image = models.ImageField('图片', upload_to='images', default='')


def upload(request):
    # a = request.POST
    # import base64
    #     # img = base64.b64decode(a['img'])
    #     # global index_img

    from django.core.files.uploadedfile import InMemoryUploadedFile
    from django.core.cache import cache
    image = request.FILES["userfile"]
    image_data = [image.file, image.field_name, image.name, image.content_type,
                  image.size, image.charset, image.content_type_extra]
    cache_key = 'image_key'
    cache.set(cache_key, image_data, 60)

    cache_data = cache.get(cache_key)
    image = InMemoryUploadedFile(*cache_data)
    Images(image=image).save()

    # img =request.FILES["userfile"]
    # index_img=0
    # path = settings.IMG_URL + str(index_img) + '.png'
    # with open(path, 'wb') as f:
    #     f.write(img)

    # index_img = index_img + 1
    # print(id(index_img))
    # print(index_img)
    #
    # from aip import AipOcr
    # import re
    # APP_ID = '17964129'
    # API_KEY = 'GlalvqRlGVrIH67fv2uxLBoT'
    # SECRECT_KEY = 'Mzt1SZj20PozVY0o7fXXiF82P0E2HaBZ'
    # client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)
    # i = open(path, 'rb')
    # img = i.read()
    # message = client.basicGeneral(img)
    # print(message)
    # # for i in message.get('words_result'):
    # #     print(i.get('words'))
    # words = message['words_result']

    return JsonResponse({"words": 1})


def search(request):
    a = request.POST.get('field')
    if a is None:
        a = ''
    print(a)
    b = ''
    b = a
    return render(request, 'search.html', locals())
