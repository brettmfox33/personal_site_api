from django.contrib import admin
from photographs.models.Album import Album
from photographs.models.Photograph import Photograph

admin.site.register(Album)
admin.site.register(Photograph)