from rest_framework import serializers
from . models import *

class chatSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = ['title', 'text']