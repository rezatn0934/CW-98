from django.db import models
from django.utils.safestring import mark_safe
from user.models import Band
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Song(models.Model):
    title = models.CharField(max_length=100)
    upload_date = models.DateTimeField(verbose_name='Upload Date', auto_now_add=True, editable=False)
    cover_photo = models.ImageField(verbose_name='Cover photo', upload_to='images/song', null=True, blank=True)
    audio_file = models.FileField(verbose_name='Audio File', upload_to='files/song')
    genres = models.ManyToManyField(Genre)
    band = models.ForeignKey(Band, on_delete=models.PROTECT, null=True, blank=True)

    @property
    def sound_display(self):
        if self.audio_file:
            return mark_safe(f'<audio controls name="media"><source src="{self.audio_file.url}" type="audio/mpeg"></audio>')
        return ""

    def cover_preview(self):
        if self.cover_photo:
            return mark_safe(f'<img src = "{self.cover_photo.url}" width = "150" height="150"/>')

    def artists(self):
        return list(self.artist_set.all())

    def genre_list(self):
        return list(self.genres.all())

    def likes(self):
        return len(self.like_set.all())

    def comments(self):
        return list(self.comment_set.filter(approved=True))

    def __str__(self):
        return self.title
