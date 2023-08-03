from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
