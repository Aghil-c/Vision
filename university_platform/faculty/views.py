from django.shortcuts import render
from faculty.models import Faculty
from coadmin.models import Coadmin
from login.models import Login
from django.core.files.storage import FileSystemStorage
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
        # obj.faculty_photo=request.POST.get('Photo')
        myfile = request.FILES['Photo']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.faculty_photo = myfile.name
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
    ss= request.session['u_id']
    obj=Faculty.objects.get(faculty_id=ss)
    context={
        'f':obj

    }
    if request.method == "POST":
        obj = Faculty.objects.get(faculty_id=ss)
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
    ss = request.session['u_id']
    obj = Faculty.objects.filter(admin_id=ss)
    context = {
        'ff': obj

    }
    return render(request,'faculty/viewfaculty.html',context)

def delete(request, idd):
    obj = Faculty.objects.get(faculty_id=idd)
    obj.delete()
    ob=Login.objects.filter(u_id=idd,type="faculty")
    ob.delete()
    return viewfaculty(request)

def accept(request,idd):
    obj=Faculty.objects.get(faculty_id=idd)
    obj.faculty_status='accepted'
    obj.save()
    return viewfaculty(request)
