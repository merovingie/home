from rest_framework import serializers
from .models import D3model

class D3modelserializer(serializers.ModelSerializer):
    class Meta:
        model = D3model
        fields = ('cx','cy', 'r', 'fill')