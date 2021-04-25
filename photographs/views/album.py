from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from photographs.models import Album
from photographs.serializers.album import AlbumSerializer, AlbumsSerializer
from django.http.response import Http404

class Albums(APIView):
    """
    List all albums, or create a new albums.
    """
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumsSerializer(albums, many=True, context={"request": request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AlbumsSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumDetails(APIView):
    """
    Get album detail
    """
    def get(self, request, uuid):
        try:
            album = Album.objects.get(pk=uuid)
        except Album.DoesNotExist:
            raise Http404

        serializer = AlbumSerializer(album, context={"request": request})
        return Response(serializer.data)
