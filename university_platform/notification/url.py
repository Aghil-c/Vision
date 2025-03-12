from django.conf.urls import url
from notification import views

urlpatterns = [
    url('post_notification/',views.notification),
    url('post_view_notification/',views.viewnotification),
    url('post_admin_notificatin/',views.admin_notification),
    url('post_view_admin_notification/',views.viewadmin_notification),


]