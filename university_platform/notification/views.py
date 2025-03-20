from django.shortcuts import render
from notification.models import Notification
from notification.models import AdminNotification
import datetime

# Create your views here.
def notification(request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=Notification()
        obj.admin_id=ss
        obj.notification=request.POST.get('notification')
        obj.notification_date=datetime.datetime.today()
        obj.notification_time=datetime.datetime.now()
        obj.save()
    return render(request,'notification/notification.html')

def viewnotification(request):
    ss=request.session['u_id']
    obj=Notification.objects.filter(admin__faculty__faculty_id=ss)
    context={
        'n': obj

    }


    return render(request,'notification/viewnotification.html',context)
def admin_notification(request):
    if request.method=='POST':
        obj=AdminNotification()
        obj.admin_notification=request.POST.get('aaa')
        obj.admin_notificationdate=datetime.datetime.today()
        obj.admin_notification_time=datetime.datetime.now()
        obj.save()
    return render(request,'notification/admin_notification.html')
def viewadmin_notification(request):
    obj=AdminNotification.objects.all()
    context = {
        'nn': obj

    }
    return render(request,'notification/view_admin_noti.html',context)