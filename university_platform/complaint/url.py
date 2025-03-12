from django.conf.urls import url
from complaint import views

urlpatterns = [
    url('post_complaintreplay/(?P<idd>\w+)',views.complaintreplay),
    url('post_complaint/',views.complaint),
    url('post_viewcomplaintreplay/',views.viwecopreplay),
    url('post_viewcomplaint/',views.viewcomplaint),


]