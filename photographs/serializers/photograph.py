from rest_framework import serializers
from photographs.models import Photograph

class PhotographSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Photograph
        fields = [
            'uuid',
            'title',
            'album',
            'photo'
        ]