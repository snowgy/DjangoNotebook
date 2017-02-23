from django.shortcuts import render
from course.models import Homework, Course
# Create your views here.


def home(request):
    course_list = Course.objects.all()
    return render(request, 'home.html', {'course_list': course_list})


def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)

    return render(request, 'course_detail.html', {'course': course})


def time_place_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'time.html', {'course': course})


def teacher_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'teacher.html', {'course': course})


def ta_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'ta.html', {'course': course})


def plan(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'plan.html', {'course': course})


def homework(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'homework.html', {'course': course})


def detail(request, course_id, homework_id):
    homework = Homework.objects.get(pk=homework_id)
    course = Course.objects.get(pk=course_id)
    return render(request, 'homework_detail.html', {'course': course, 'homework': homework})


def pre(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'pre.html', {'course': course})


def pro(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'pro.html', {'course': course})







