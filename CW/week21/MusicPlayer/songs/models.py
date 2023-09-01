from django.db import models
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
    band = models.ForeignKey(Band, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

