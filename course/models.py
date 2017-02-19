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


class Pre(models.Model):
    topic = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)
    pre_time = models.DateField(auto_now_add=False, auto_now=False)
    plan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ['-date_time']


class Pro(models.Model):
    topic = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)
    pre_time = models.DateField(auto_now_add=False, auto_now=False)
    plan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ['-date_time']


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    contact_information = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=20)
    reservation = models.DateTimeField(auto_now=False, auto_now_add=False)


class TA(models.Model):
    name = models.CharField(max_length=50)
    contact_information = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=20)
    reservation = models.DateTimeField(auto_now=False, auto_now_add=False)


class Course(models.Model):
    title = models.CharField(max_length=50, null=True)
    place_time = models.TextField(null=True, blank=True)
    tutorial_place_time = models.TextField(null=True, blank=True)
    homework = models.ManyToManyField(Homework)
    pre = models.ManyToManyField(Pre)
    pro = models.ManyToManyField(Pro)
    teacher = models.ManyToManyField(Teacher)
    ta = models.ManyToManyField(TA)

    def __str__(self):
        return self.title