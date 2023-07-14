from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Category(models.Model):
     name = models.CharField(max_length=50)
     description = models.TextField()

     def __str__(self):
         return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.post + "/" + self.author