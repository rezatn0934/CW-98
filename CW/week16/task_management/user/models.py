from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe
from .mixins import ImageMixin

# Create your models here.


class CustomUser(ImageMixin, AbstractUser):
    image = models.ImageField(upload_to='images/product/', blank=True, null=True)

    def img_preview(self):
        if self.image:
            return mark_safe(f'<img src = "{self.image.url}" width = "150" height="150"/>')

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = CustomUser.objects.get(pk=self.pk)
            self.change_image(old_instance, "image")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            self.delete_image("image")
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.username
