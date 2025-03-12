from django.shortcuts import render
from calender.models import Calender

# Create your views here.
def calender(request):
    if request.method=='POST':
        obj=Calender()
        obj.calender_name=request.POST.get('name')
        obj.calender_date=request.POST.get('date')
        obj.calender_description=request.POST.get('description')
        obj.calender_time=request.POST.get('time')
        obj.save()

    return render(request,'calender/calender.html')
def viewcalender(request):
    obj=Calender.objects.all()
    context={
        'a':obj

    }
    return render(request,'calender/viewcalender.html',context)

def admin_calender(request):
    if request.method=='POST':
        obj=Calender()
        obj.calender_name=request.POST.get('name')
        obj.calender_date=request.POST.get('date')
        obj.calender_description=request.POST.get('description')
        obj.calender_time=request.POST.get('time')
        obj.save()

    return render(request, 'calender/admin_calender.html')
def viewadmincalender(request):
    obj=Calender.objects.all()
    context={
        'a':obj

    }
    return render(request,'calender/view_admincalender.html',context)