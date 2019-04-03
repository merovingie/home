from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
import json, os
from django.conf import settings
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import viewsets
from .serializers import CommandsSerializer


class jsontoangular(viewsets.ModelViewSet):
    queryset = Commands.objects.all()
    serializer_class = CommandsSerializer




