
from django.core.paginator import Paginator
from django.shortcuts import redirect, reverse, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from .mixins import LikeMixin
from .models import Song
from user.models import Artist
from social.forms import CommentCreation


# Create your views here.


class Home(ListView):
    template_name = 'song/songs.html'
    model = Song
    context_object_name = 'songs'
    object_list = None

