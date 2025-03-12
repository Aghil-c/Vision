from django.conf.urls import url
from course import views

urlpatterns = [
    url('post_course/',views.course),
    url('post_viewcourse/',views.viewcourse),
    url('delete/(?P<idd>\w+)', views.delete),
    url('delete_course/',views.delete_course),


]