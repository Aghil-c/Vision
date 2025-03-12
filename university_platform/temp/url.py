from django.conf.urls import url
from temp import views

urlpatterns = [

    url('post_admintemp/',views.admintemp),
    url('post_co_admin/',views.co_admin),
    url('post_home/',views.home),
    url('post_staff/',views.staff),


]