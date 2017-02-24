from django.conf.urls import url
from django.contrib import admin
from . import views


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
    url(r'^create/$', views.create_page, name='create_page'),
    url(r'^create/action/$', views.create_action, name='create_action'),
    url(r'^edit_time/(?P<course_id>\d+)$', views.edit_page, name='time_edit'),
    url(r'^edit_time/action/$', views.edit_time_action, name='edit_time_action'),

]