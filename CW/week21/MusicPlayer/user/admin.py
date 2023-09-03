from django.contrib import admin
from .models import AbstractUser, Band, Artist, Listener
from .forms import ArtistRegisterForm


admin.site.site_header = 'Music Player Management'
admin.site.site_title = 'Colorlib Management'
admin.site.index_title = 'Welcome to admin panel'


