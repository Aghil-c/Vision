from django.conf.urls import url
from study_meterial import views

urlpatterns = [
    url('post_stydy_meterial/',views.studymeterial),
    url('post_view_study_meterial/',views.viewstdymet),
    url('post_view_student_study/',views.view_student_study),
    url('delete/(?P<idd>\w+)', views.delete),
    url('admin_view_study/',views.view_admin_study),


]