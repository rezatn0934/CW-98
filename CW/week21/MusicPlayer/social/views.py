from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView

from .forms import CommentCreation
from .models import Like, Comment
from songs.models import Song


# Create your views here.


class LikeView(View):

    def post(self, request):
        song_id = request.POST.get('like')
        is_like = request.POST.get('like_input')
        if is_like == 'like':
            Like.objects.create(user_id=request.user.id, song_id=song_id)
        elif is_like == 'unlike':
            Like.objects.filter(user_id=request.user.id, song_id=song_id).delete()

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

        return JsonResponse({'message': 'successfully created'}, status=200)

    def form_invalid(self, form):
        data = {'error': form.errors}
        return JsonResponse(data, status=400)
