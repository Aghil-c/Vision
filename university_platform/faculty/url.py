from django.conf.urls import url
from faculty import views

urlpatterns = [
    url('post_faculty/',views.faculty),
    url('post_view_faculty/',views.viewfaculty),
    url('update/',views.update),
    url('delete/(?P<idd>\w+)', views.delete),
    url('accept/(?P<idd>\w+)',views.accept),


]