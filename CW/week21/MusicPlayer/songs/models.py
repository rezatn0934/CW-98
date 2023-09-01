from django.db import models
from user.models import Band
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100)


