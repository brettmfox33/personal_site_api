import uuid

from django.db import models
from photographs.models.Album import Album


class Photograph(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='photo')
    album = models.ForeignKey(Album, on_delete=models.PROTECT)