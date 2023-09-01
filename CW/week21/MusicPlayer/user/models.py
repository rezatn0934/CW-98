from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from manger import UserManager
from songs.models import Song


class AbstractUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    name = models.CharField(verbose_name=_("First Name"), max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='images/user', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name=_("Joined Date"), auto_now_add=True)
    last_modify = models.DateTimeField(verbose_name=_("Last Modify"), auto_now=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        abstract = True


