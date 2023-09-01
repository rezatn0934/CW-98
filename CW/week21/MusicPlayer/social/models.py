from django.db import models
from django.db import models
from user.models import User
from songs.models import Song
# Create your models here.


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.song}"
