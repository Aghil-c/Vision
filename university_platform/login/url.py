from django.conf.urls import url
from login import views

urlpatterns = [
    url('post_login/',views.login),
    # url('sign_up/',views.login),



]