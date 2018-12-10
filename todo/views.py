from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Todo
import json, os
from django.conf import settings
from django.core import serializers


def todo(request):
    todos = Todo.objects
    return render(request, 'todo/todo.html',{'todos' : todos})

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
        buff = serializers.serialize("json", Todo.objects.all())
        fileIN = str(buff)
        #SYS = json.dump(fileIN, global_file_path, ensure_ascii=False)
        outfile.write(fileIN)
        #json.dump(data, global_file_path)


    return JsonResponse(buff, safe=False)
