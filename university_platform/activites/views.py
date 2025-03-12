from django.shortcuts import render
from activites.models import Activities
import datetime
# Create your views here.
def activity(request):
    if request.method=="POST":
        obj=Activities()
        obj.faculty_id=1
        obj.student_id=1
        obj.activities=request.POST.get('activity')
        obj.activities_name=request.POST.get('activity_name')
        obj.activity_date=datetime.datetime.today()
        obj.activity_time=datetime.datetime.now()
        obj.save()
    return render(request,'activites/activity.html')

def response(request,idd):
    if request.method=="POST":
        obj=Activities.objects.get(activities_id=idd)
        obj.faculty_id=1
        obj.student_id=1
        obj.activities_response=request.POST.get('file')
        obj.activity_date = datetime.datetime.today()
        obj.activity_time = datetime.datetime.now()
        obj.save()
    return render(request,'activites/response.html')

def viewactivityresponse(request):
    obj=Activities.objects.all()
    context={
        'bbbbb':obj
    }
    return render(request,'activites/viewactivityresponse.html',context)

def viewaddactivity(request):
    obj=Activities.objects.all()
    context={
        'aaaaaaaa':obj
    }
    return render(request,'activites/viewadd_activity.html',context)

def delete_actvity(request):
    obj=Activities.objects.all()
    context={
        'aaaaaaa':obj
    }
    return render(request,'activites/delete_actvity.html',context)


def delete(request,idd):
    obj = Activities.objects.get(activities_id=idd)
    obj.delete()
    return delete_actvity (request)

def admin_viewactivity(request):
    obj=Activities.objects.all()
    context={
        'aaaaaaaa':obj
    }
    return render(request,'activites/admin_viewactivity.html',context)
