from django.conf.urls import url
from photo_video import views

urlpatterns = [
    url('post_video/',views.video),
    url('post_photo_video/',views.photovideo),


]