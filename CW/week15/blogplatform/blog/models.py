from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
     name = models.CharField(max_length=50)
     description = models.TextField()

     def __str__(self):
         return self.name

class Comment(models.Model):
    post = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.post + "/" + self.author