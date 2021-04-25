from rest_framework import serializers
from photographs.models import Album
from photographs.serializers.photograph import PhotographSerializer

class AlbumsSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name='album', lookup_field='uuid')
    photographs = PhotographSerializer(many=True, read_only=True, source='photograph_set')

    class Meta:
        model = Album
        fields = [
            'uuid',
            'title',
            'date',
            'description',
            'cover_photo',
            'detail',
            'location',
            'photographs'
        ]

class AlbumSerializer(serializers.ModelSerializer):
    photographs = PhotographSerializer(many=True, read_only=True, source='photograph_set')

    class Meta:
        model = Album
        fields = [
            'uuid',
            'title',
            'date',
            'description',
            'cover_photo',
            'photographs',
            'location'
        ]