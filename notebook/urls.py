"""notebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from course import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^homework$', views.homework, name='homework'),
    url(r'^course/(?P<course_id>\d+)/$', views.course_detail, name='course'),
    url(r'^time_place/(?P<course_id>\d+)/$', views.time_place_detail, name='time'),
    url(r'^teacher/(?P<course_id>\d+)/$', views.teacher_detail, name='teacher'),
    url(r'^ta/(?P<course_id>\d+)/$', views.ta_detail, name='ta'),
    url(r'^plan/(?P<course_id>\d+)/$', views.plan, name='plan'),
    url(r'^homework/(?P<course_id>\d+)/$', views.homework, name='homework'),
    url(r'^detail/(?P<course_id>\d+)/(?P<homework_id>\d+)/$', views.detail, name='detail'),
    url(r'^pre/(?P<course_id>\d+)/$', views.pre, name='pre'),
    url(r'^pro/(?P<course_id>\d+)/$', views.pro, name='pro'),

]
