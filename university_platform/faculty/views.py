from django.shortcuts import render
from faculty.models import Faculty
from coadmin.models import Coadmin
from login.models import Login
# Create your views here.
def faculty(request):
    obj = Coadmin.objects.all()
    context = {
        'f': obj

    }
    if request.method=="POST":
        obj=Faculty()
        obj.faculty_email=request.POST.get('Email')
        obj.faculty_gender=request.POST.get('gender')
        obj.faculty_password=request.POST.get('Password')
        obj.faculty_photo=request.POST.get('Photo')
        obj.faculty_username=request.POST.get('User')
        obj.faculty_name=request.POST.get('Name')
        obj.faculty_phonel=request.POST.get('number')
        obj.admin_id=request.POST.get('coadmin')
        obj.save()
        ob=Login()
        ob.username=obj.faculty_username
        ob.password=obj.faculty_password
        ob.u_id=obj.faculty_id
        ob.type='faculty'
        ob.save()

    return render(request,'faculty/faculty.html',context)
def update(request):
    obj=Faculty.objects.get(faculty_id=3)
    context={
        'f':obj

    }
    if request.method == "POST":
        obj = Faculty.objects.get(faculty_id=3)
        obj.faculty_email = request.POST.get('Email')
        obj.faculty_gender = request.POST.get('gender')
        obj.faculty_password = request.POST.get('Password')
        obj.faculty_photo = request.POST.get('Photo')
        obj.faculty_username = request.POST.get('User')
        obj.faculty_name = request.POST.get('Name')
        obj.faculty_phonel = request.POST.get('number')
        obj.admin_id = 1
        obj.save()

    return render(request,'faculty/update.html',context)
def viewfaculty(request):
    obj = Faculty.objects.all()
    context = {
        'ff': obj

    }
    return render(request,'faculty/viewfaculty.html',context)

def delete(request, idd):
    obj = Faculty.objects.get(faculty_id=idd)
    obj.delete()
    return viewfaculty(request)

def accept(request,idd):
    obj=Faculty.objects.get(faculty_id=idd)
    obj.faculty_status='accepted'
    obj.save()
    return viewfaculty(request)
