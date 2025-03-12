from django.conf.urls import url
from doubts import views

urlpatterns = [
    url('post_dubt/',views.doubt),
    url('post_doubtreplay/(?P<idd>\w+)',views.doubtreplay),
    url('post_viewdoubtreplay/',views.viewdoubtreplay),
    url('post_viewdoubt/',views.viewdoubt),



]