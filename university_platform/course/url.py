from django.conf.urls import url
from course import views

urlpatterns = [
    url('post_course/',views.course),
    url('post_viewselectcourse/',views.viewcourse),
    url('delete/(?P<idd>\w+)', views.delete),
    url('delete_course/',views.delete_course),
    url('select_course/',views.select_course),
    url('select/(?P<idd>\w+)',views.selectcoursebyco),
    url('aaaaaa/(?P<idd>\w+)', views.deletes),
    url('delete_selectcourse/',views.deletes_course)


]