from django.conf.urls import url
from activites import views

urlpatterns=[
    url('post_activity/',views.activity),
    url('post_response/(?P<idd>\w+)',views.response),
    url('post_view_activity_response/',views.viewactivityresponse),
    url('post_viewaddactivity/',views.viewaddactivity),
    url('delete/(?P<idd>\w+)', views.delete),
    url('delete_actvity/',views.delete_actvity),
    url('admin_viewactivity/',views.admin_viewactivity),


]