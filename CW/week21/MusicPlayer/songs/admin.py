from django.contrib import admin
from django.db.models import Count, F

from .models import Song, Genre
from user.models import Artist


class UserInline(admin.TabularInline):
    model = Artist.songs.through


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_artists', 'sound_display', 'band_name', 'upload_date', 'cover_preview')
    inlines = [UserInline, ]
    list_filter = ('title__istartwith', 'upload_date__istartwith')

    list_select_related = ('band', 'artist')

    def band_name(self, obj):
        if obj.band:
            return obj.band.name

    band_name.short_description = 'Band Name'

    def sound_display(self, item):
        return item.sound_display

    sound_display.short_description = 'Audio'

    def display_artists(self, obj):
        artists = obj.artist_set.all()
        artist_names = [artist.username for artist in artists]
        return ', '.join(artist_names)

    display_artists.short_description = 'Artists'
