from django.conf.urls import url
from feedback import views

urlpatterns = [
    url('post_view_feedback/',views.viewfeedback),


]