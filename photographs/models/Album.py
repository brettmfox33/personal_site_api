import uuid
from django.db import models

class Album(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=256)
    cover_photo = models.ImageField(upload_to='album')
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title