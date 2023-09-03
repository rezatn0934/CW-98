from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.db import models

from .manger import UserManager


class AbstractUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=25)
    name = models.CharField(verbose_name=_("Name"), max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name=_("Joined Date"), auto_now_add=True)
    last_modify = models.DateTimeField(verbose_name=_("Last Modify"), auto_now=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.username


class Band(models.Model):
    name = models.CharField(max_length=50)
    start_at = models.DateTimeField(auto_now_add=True, editable=False)
    end_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Artist(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    songs = models.ManyToManyField('songs.Song')
    band = models.ForeignKey(Band, on_delete=models.PROTECT, null=True, blank=True)
    image = models.ImageField(upload_to='images/artist', null=True, blank=True)

    def img_preview(self):
        if self.image:
            return mark_safe(f'<img src = "{self.image.url}" width = "150" height="150"/>')

    def __str__(self):
        return f"artist - {self.username}"


class Listener(AbstractUser):
    image = models.ImageField(upload_to='images/listener', null=True, blank=True)
    USER_STATUS_VIP = 'V'
    USER_STATUS_FREE = 'F'
    USER_STATUS_CHOICES = [
        (USER_STATUS_VIP, 'VIP'),
        (USER_STATUS_FREE, 'FREE'),
    ]
    user_status = models.CharField(max_length=1, choices=USER_STATUS_CHOICES, default=USER_STATUS_FREE)
    vip_until = models.DateTimeField(null=True, blank=True)

    def img_preview(self):
        if self.image:
            return mark_safe(f'<img src = "{self.image.url}" width = "150" height="150"/>')

