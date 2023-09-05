from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AbstractUser, Artist, Listener, Band
from .forms import ArtistRegisterForm, ListenerRegisterForm, CustomUserCreationForm, CustomUserChangeForm

admin.site.site_header = 'Music Player Management'
admin.site.site_title = 'Colorlib Management'
admin.site.index_title = 'Welcome to admin panel'


@admin.register(AbstractUser)
class AbstractUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = [
        [None, {'fields': ['username', 'email', 'password1', 'password2']}],
        ['Personal Info', {'fields': ['name', ]}],
        ['Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser']}],
    ]
    add_fieldsets = [
        [None, {'fields': ['username', 'email', 'password1', 'password2']}],
        ['Personal Info', {'fields': ['name', ]}],
        ['Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser']}],
    ]

    list_display = ['username', 'email', 'name', 'last_login', 'date_joined', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['username__istartwith', 'email__istartswith', 'name__istartswith']
    ordering = ['date_joined', ]


@admin.register(Artist)
class ArtistUserAdmin(AbstractUserAdmin):
    form = ArtistRegisterForm
    model = Artist

    list_display = ['name', 'songs_list', 'bio', 'band_name', 'username', 'email', 'is_active', 'is_staff',
                    'is_superuser', 'last_login', 'date_joined', 'img_preview']
    list_select_related = ['band', ]
    fieldsets = (
        *AbstractUserAdmin.fieldsets,
        ('Artist Info', {'fields': ('bio', 'band', 'songs')}),
    )
    add_fieldsets = (
        *AbstractUserAdmin.add_fieldsets,
        ('Artist Info', {
            'fields': ('bio', 'band', 'songs'),
        }),
    )
    search_fields = ['username__istartwith', 'email__istartswith', 'name__istartswith']
    ordering = ['date_joined', ]

    def songs_list(self, obj):
        return ",".join([song.title for song in obj.songs.all()])
    songs_list.short_description = 'Songs List'


    def band_name(self, obj):
        if obj.band:
            return obj.band.name

    band_name.short_description = 'Band Name'


@admin.register(Listener)
class ListenerUserAdmin(AbstractUserAdmin):
    form = ListenerRegisterForm
    modl = Listener
    list_display = ['name', 'user_status', 'vip_until', 'username', 'email', 'is_active', 'is_staff',
                    'is_superuser', 'last_login', 'date_joined', 'img_preview']
    search_fields = ['username__istartwith', 'email__istartswith', 'name__istartswith']
    ordering = ['date_joined', ]

    fieldsets = (
        *AbstractUserAdmin.fieldsets,
        ('Listener Info', {'fields': ('user_status', 'vip_until')}),
    )
    add_fieldsets = (
        *AbstractUserAdmin.add_fieldsets,
        ('Listener Info', {
            'fields': ('user_status', 'vip_until'),
        }),
    )
