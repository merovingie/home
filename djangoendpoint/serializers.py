from rest_framework import serializers
from .models import *

class CommandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commands
        fields = ('command','paramters', 'argumentsProv ')