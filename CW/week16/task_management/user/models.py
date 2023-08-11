from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe


# Create your models here.


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='images/product/', blank=True, null=True)

    def img_preview(self):
        if self.image:
            return mark_safe(f'<img src = "{self.image.url}" width = "150" height="150"/>')

    def __str__(self):
        return self.username
