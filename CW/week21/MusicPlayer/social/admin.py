from django.contrib import admin
from django.template.defaultfilters import truncatewords

from .models import Playlist, Like, Comment

# Register your models here.


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'truncated_description', 'owner_user', 'songs_list')
    list_filter = ('title', 'owner', )
    search_fields = ('title__istartwith', 'owner__name__istartwith', )
    list_select_related = ('owner', )
    list_per_page = 30

    def owner_user(self, obj):
        return obj.owner.username

    def songs_list(self, obj):
        return ",".join([song.title for song in obj.songs.all()])

    def truncated_description(self, obj):
        if obj.description:
            return truncatewords(obj.description, 10)
