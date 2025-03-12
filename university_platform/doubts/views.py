from django.shortcuts import render
from doubts.models import Doubt
import datetime

# Create your views here.
def doubtreplay(request,idd):
    if request.method=="POST":
        obj=Doubt.objects.get(doubt_id=idd)
        obj.doubt_replayl=request.POST.get('un')
        obj.save()
    return render(request,'doubts/doubtreplay.html')
def doubt(request):
    if request.method == "POST":
        obj=Doubt()
        obj.faculty_id=1
        obj.student_id=1
        obj.doubt=request.POST.get('doubt')
        obj.doubt_date = datetime.datetime.today()
        obj.doubt_time = datetime.datetime.now()
        obj.save()
    return render(request, 'doubts/doubt.html')
def viewdoubtreplay(request):
    obj=Doubt.objects.all()
    context={
        'd':obj
    }
    return render(request,'doubts/viewdoubt_replay.html',context)
def viewdoubt(request):
    obj = Doubt.objects.all()
    context = {
        'dd': obj
    }
    return render(request,'doubts/viewdoubts.html',context)