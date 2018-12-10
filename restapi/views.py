from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import D3model
import json, os
from django.conf import settings
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


def jsontojs(request):
    #buff = Todo.objects
    #local_file_path = '{0}/{1}/{2}'.format(resolve(request.path).todo 'statics', 'd.json')
    # data = {
    #     'r': buff.radius,
    #     'cx': buff.x,
    #     'cy': buff.y,
    #     'fill': 'pink'
    # }
    global_file_path = os.path.join(settings.STATIC_ROOT, 'd.json')

    with open( global_file_path , 'w') as outfile:
        buff = serializers.serialize("json", Todo.objects.all(), fields=('r','cx','cy','fill'), cls=DjangoJSONEncoder, ensure_ascii=False)
        #fileIN = str(buff)
        #SYS = json.dump(fileIN, global_file_path, ensure_ascii=False)
        outfile.write(buff)
        #json.dump(data, global_file_path)


    return JsonResponse(buff, safe=False)