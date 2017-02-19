from django.shortcuts import render
from course.models import Homework, Course
# Create your views here.


def home(request):
    course_list = Course.objects.all()
    return render(request, 'home.html', {'course_list': course_list})


def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'course.html', {'course': course})


def homework(request):
    course = Course.objects.all()
    homework_list = Homework.objects.all()
    return render(request, 'homework.html', {'homework_list': homework_list})





