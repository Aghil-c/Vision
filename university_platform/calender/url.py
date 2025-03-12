from django.conf.urls import url
from calender import views

urlpatterns = [
      url('post_calender/',views.calender),
      url('post_view_calender/',views.viewcalender),
      url('post_admin_calender/',views.admin_calender),
      url('view_admin_calender/',views.viewadmincalender),

]