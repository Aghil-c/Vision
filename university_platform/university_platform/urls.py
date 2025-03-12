"""university_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    url('activites/',include('activites.url')),
    url('coadmin/', include('coadmin.url')),
    url('calender/',include('calender.url')),
    url('chat/',include('chat.url')),
    url('complaint/',include('complaint.url')),
    url('course/',include('course.url')),
    url('doubts/',include('doubts.url')),
    url('faculty/',include('faculty.url')),
    url('feedback/',include('feedback.url')),
    url('group/',include('group.url')),
    url('login/',include('login.url')),
    url('notification/',include('notification.url')),
    url('photo_video/',include('photo_video.url')),
    url('student/',include('student.url')),
    url('study_meterial/',include('study_meterial.url')),
    url('temp/',include('temp.url'))


]
