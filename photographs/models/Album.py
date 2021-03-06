import uuid
from django.db import models
from photographs.utils import store_album_image

class Album(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=256)
    cover_photo = models.ImageField(upload_to=store_album_image)
    date = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.title