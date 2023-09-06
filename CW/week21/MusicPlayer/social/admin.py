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


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_username', 'song_title')
    search_fields = ('user_username__istartwith', 'song_title__istartwith')
    list_per_page = 50
    list_select_related = ('user', 'song', )

    def user_username(self, obj):
        return obj.user.username

    def song_title(self, obj):
        return obj.song.title


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_username', 'song_title', 'content_description', 'approved')
    list_filter = ('song__title', )
    search_fields = ('user_username__istartwith', 'song_title__istartwith')

    def user_username(self, obj):
        return obj.user.username

    def song_title(self, obj):
        return obj.song.title

    def content_description(self, obj):
        if obj.content:
            return truncatewords(obj.content, 10)