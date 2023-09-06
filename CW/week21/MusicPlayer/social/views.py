import logging
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.generic import CreateView
from django.views import View

from .forms import CommentCreation, PlaylistCreation
from .models import Like, Comment, Playlist
from songs.models import Song

logger = logging.getLogger('django')


# Create your views here.

class LikeView(View):
    def post(self, request):
        song_id = request.POST.get('like')
        is_like = request.POST.get('like_input')
        if is_like == 'like':
            Like.objects.create(user_id=request.user.id, song_id=song_id)
            logger.info(f"User {request.user.username} liked song with ID {song_id}")
        elif is_like == 'unlike':
            Like.objects.filter(user_id=request.user.id, song_id=song_id).delete()
            logger.info(f"User {request.user.username} unliked song with ID {song_id}")

        like_count = Song.objects.get(id=song_id).likes()
        return JsonResponse({'like_count': like_count}, status=200)


class CreatCommentView(CreateView):
    model = Comment
    form_class = CommentCreation

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        song_id = self.request.POST.get('song_id')
        comment.song = Song.objects.get(id=int(song_id))
        comment.save()

        subject = 'Comment'
        message = ('Your Comment has been successfully created. '
                   'after admin confirmation will be displayed on website')
        recipient_list = self.request.user.email
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, recipient_list)
        logger.info(f"User {self.request.user.username} created a comment on song with ID {song_id}")
        return JsonResponse({'message': 'successfully created'}, status=200)

    def form_invalid(self, form):
        data = {'error': form.errors}
        return JsonResponse(data, status=400)


class CreatPlayListView(CreateView):
    model = Playlist
    form_class = PlaylistCreation

    def form_valid(self, form):
        playlist = form.save(commit=False)
        playlist.owner = self.request.user
        playlist.save()

        subject = 'Playlist created'
        message = 'Your Playlist has been successfully created.'
        recipient_list = [self.request.user.email, ]
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, recipient_list)
        data = {'id': playlist.id, 'title': playlist.title, 'message': 'successfully created'}
        logger.info(f"User {self.request.user.username} created a playlist with ID {playlist.id}")
        return JsonResponse(data, status=200)

    def form_invalid(self, form):
        data = {'error': form.errors}
        return JsonResponse(data, status=400)


class UpdatePlayListView(View):
    model = Playlist

    def post(self, request):
        song_id = request.POST.get('song_id')
        song = Song.objects.get(id=song_id)
        playlist_id = request.POST.get('playlist_input')
        playlist = self.model.objects.get(id=playlist_id)
        playlist.songs.add(song)

        subject = 'Add song to play list'
        message = f'Song ({song.title}) has been successfully added to Playlist ({playlist.title})'
        recipient_list = [request.user.email, ]
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, recipient_list)
        logger.info(f"User {request.user.username} added song with ID {song_id} to playlist with ID {playlist_id}")
        return JsonResponse({'message': 'successfully added'}, status=200)
