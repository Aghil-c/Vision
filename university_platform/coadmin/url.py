from django.conf.urls import url
from coadmin import views

urlpatterns=[
   url('post_admin/',views.adminn),
   url('post_view_admin/',views.view_adminn),
   url('delete/(?P<idd>\w+)', views.delete),
   url('accept/(?P<idd>\w+)', views.accept),
]