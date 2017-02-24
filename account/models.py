from django.db import models
from django.contrib import admin
from course.models import Course

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    course = models.ManyToManyField(Course, blank=True)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', )
