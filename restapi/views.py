from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import D3model
import json, os
from django.conf import settings
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import viewsets
from .serializers import D3modelserializer


class jsontojs(viewsets.ModelViewSet):
    queryset = D3model.objects.all()
    serializer_class = D3modelserializer



    def jsontojsView(buff):
        global_file_path = os.path.join(settings.STATIC_ROOT, 'd.json')
        buff = serializer_class
        with open( global_file_path , 'w') as outfile:
            outfile.write(buff)
            # buff = serializers.serialize("json", Todo.objects.all(), fields=('r','cx','cy','fill'), cls=DjangoJSONEncoder, ensure_ascii=False)
        return JsonResponse(buff, safe=False)


    



