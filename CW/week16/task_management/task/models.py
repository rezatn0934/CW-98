from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label


class Task(models.Model):
    STATUS_UNASSIGNED = 'U'
    STATUS_ASSIGNED = 'A'
    STATUS_IN_PROGRESS = 'I'
    STATUS_COMPLETE = 'C'

    STATUS_CHOICES = [
        (STATUS_UNASSIGNED, 'Unassigned'),
        (STATUS_ASSIGNED, 'Assigned'),
        (STATUS_IN_PROGRESS, 'In_Progress'),
        (STATUS_COMPLETE, 'Completed'),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default=STATUS_UNASSIGNED)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


