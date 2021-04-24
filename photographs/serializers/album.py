from rest_framework import serializers
from photographs.models import Album

class AlbumSerializer(serializers.ModelSerializer):
    # cover_photo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Album
        fields = [
            'uuid',
            'title',
            'date',
            'description',
            'cover_photo',
            # 'cover_photoc_url'
        ]

    def get_cover_photo_url(self, instance):
        request = self.context.get("request")
        return request.build_absolute_uri(instance.cover_photo.url)