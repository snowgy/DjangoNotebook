from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Homework(models.Model):
    title = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)
    due_time = models.DateField(auto_now=False, auto_now_add=False)
    content = models.TextField(blank=True, null=True)
    plan = models.TextField(blank=True, null=True)
    question = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


class Course(models.Model):
    title = models.CharField(max_length=50, null=True)
    homework = models.ManyToManyField(Homework)

    def __str__(self):
        return self.title