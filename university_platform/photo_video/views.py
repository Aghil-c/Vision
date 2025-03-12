from django.shortcuts import render
from photo_video.models import PhotoVideo
import datetime
# Create your views here.
def video(request):
    if request.method == "POST":
        obj = PhotoVideo()
        obj.student_id=1
        obj.faculty_id=1
        obj.pv=request.POST.get('uploadfile')
        obj.title=request.POST.get('study')
        obj.pv_date=datetime.datetime.today()
        obj.pv_time=datetime.datetime.now()
        obj.save()
    return render(request,'photo_video/video.html')
def photovideo(request):
    obj=PhotoVideo.objects.all()
    context={
        'pv':obj
    }
    return render(request,'photo_video/viewphotovideo.html',context)


def delete(request,idd):
    obj = PhotoVideo.objects.get(course_id=idd)
    obj.delete()
    return PhotoVideo (request)