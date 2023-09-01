from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models

from .manger import UserManager


class AbstractUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    name = models.CharField(verbose_name=_("Name"), max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='images/user', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name=_("Joined Date"), auto_now_add=True)
    last_modify = models.DateTimeField(verbose_name=_("Last Modify"), auto_now=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
    objects = UserManager()


class Band(models.Model):
    name = models.CharField(max_length=50)
    start_at = models.DateTimeField(auto_now_add=True, editable=False)
    end_at = models.DateTimeField(blank=True, null=True, editable=True)


class Artist(AbstractUser):
    bio = models.TextField()
    songs = models.ManyToManyField('songs.Song')
    band = models.ForeignKey(Band, on_delete=models.PROTECT)


class Listener(AbstractUser):
    is_vip = models.BooleanField(default=True)
