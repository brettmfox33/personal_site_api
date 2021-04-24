from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from photographs.models import Photograph
from photographs.serializers.photograph import PhotographSerializer
from django.http.response import Http404

class Photographs(APIView):
    """
    List all Photographs, or create a new photograph.
    """
    def get(self, request, album_id):
        photographs = Photograph.objects.filter(album=album_id)
        serializer = PhotographSerializer(photographs, many=True, context={"request": request})
        return Response(serializer.data)
    
    def post(self, request, album_id):
        serializer = PhotographSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
