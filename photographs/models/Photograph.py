import uuid

from django.db import models
from photographs.models.Album import Album
from photographs.utils import store_photograph_image


class Photograph(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=256)
    photo = models.ImageField(upload_to=store_photograph_image)
    album = models.ForeignKey(Album, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.album.title} - {self.title}"