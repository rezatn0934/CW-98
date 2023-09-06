from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .mixins import LikeMixin

from .models import Song
from user.models import Artist
from social.forms import CommentCreation, PlaylistCreation
from social.models import Playlist


# Create your views here.


class Home(LikeMixin, ListView):
    template_name = 'song/songs.html'
    model = Song
    context_object_name = 'songs'
    object_list = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artists'] = Artist.objects.all()
        context['playlists'] = Playlist.objects.filter(owner=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('search')

        items = self.get_queryset()
        if request.headers.get('HX-Request') == 'true':
            self.template_name = 'song/search_result.html'
            if isinstance(search_term, str):
                if search_term != '':
                    items = items.filter(title__icontains=search_term)
                    if not items.exists():
                        items = ["Nothing Was Found"]

        paginator = Paginator(items, 15)

        page_number = request.GET.get("page")
        items = paginator.get_page(page_number)
        context = self.get_context_data(**kwargs)
        context.update({'songs': items, 'page': page_number, 'search': search_term})

        return render(request, self.template_name, context=context)


class SongDetailView(LikeMixin, DetailView):
    model = Song
    template_name = 'song/song_detail.html'
    context_object_name = 'song'
    form_class = CommentCreation
    login_url = reverse_lazy('user:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        context['form1'] = PlaylistCreation()
        context['playlists'] = Playlist.objects.filter(owner=self.request.user)
        return context
