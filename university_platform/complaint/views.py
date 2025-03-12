from django.shortcuts import render
from complaint.models import Complaint
import datetime

# Create your views here.
def complaintreplay(request,idd):
    if request.method == 'POST':
        obj=Complaint.objects.get(complaint_id=idd)
        obj.complaint_replay=request.POST.get('replay')
        obj.save()

    return render(request,'complaint/complaintreplay.html')
def complaint(request):
    if request.method=="POST":
        obj=Complaint()
        obj.complaint_name=request.POST.get('Complaintname')
        obj.complaint_date=datetime.datetime.today()
        obj.complaint_time=datetime.datetime.now()
        obj.complaint=request.POST.get('Complaint')
        obj.complaint_replay="pending"
        obj.admin_id=1
        obj.faculty_id=1
        obj.save()
    return render(request,'complaint/complaints.html')
def viwecopreplay(request):
    obj=Complaint.objects.all()
    context={
        'bb':obj
    }



    return render(request,'complaint/viewcomp_replay.html',context)
def viewcomplaint(request):
    obj = Complaint.objects.all()
    context = {
        'bbb': obj
    }

    return render(request,'complaint/viewcomplaint.html',context)