from django.db import models
from user.models import AbstractUser
from songs.models import Song
# Create your models here.


class Playlist(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title

    def song_list(self):
        return list(self.songs.all())


class Like(models.Model):
    user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.song}"


class Comment(models.Model):
    user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()
    approved = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"{self.user} - {self.song}"
