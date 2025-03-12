from django.shortcuts import render
from study_meterial.models import StudyMaterial
import datetime
# Create your views here.
def studymeterial(request):
    if request.method == "POST":
        obj=StudyMaterial()
        obj.faculty_id=1
        obj.study_materialdes=request.POST.get('study')
        obj.study_material=request.POST.get('uploadfile')
        obj.study_date=datetime.datetime.today()
        obj.study_time=datetime.datetime.now()
        obj.save()
    return render(request,'study_meterial/studymeterial.html')

def viewstdymet(request):
    obj=StudyMaterial.objects.all()
    context={
        'ss':obj
    }
    return render(request,'study_meterial/view_studymeterial.html',context)
def view_student_study(request):
    obj=StudyMaterial.objects.all()
    context={
        'sss':obj
    }
    return render(request, 'study_meterial/view_student_study.html', context)
def delete(request, idd):
    obj = StudyMaterial.objects.get(study_id=idd)
    obj.delete()
    return viewstdymet (request)
def view_admin_study(request):
    obj=StudyMaterial.objects.all()
    context={
        'sss':obj
    }
    return render(request, 'study_meterial/study_admin.html', context)
