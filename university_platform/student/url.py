from django.conf.urls import url
from student import views

urlpatterns = [
    url('post_view_student/',views.viewstudents),
    url('delete/(?P<idd>\w+)', views.delete),
    url('view_staff_student/',views.view_staff_student),




]