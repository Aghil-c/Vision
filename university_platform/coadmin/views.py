from django.shortcuts import render
from coadmin.models import Coadmin
from django.core.files.storage import FileSystemStorage
from login.models import Login


# Create your views here.
def adminn(request):
    if request.method=='POST':
        obj=Coadmin()
        obj.admin_college=request.POST.get('college')
        obj.admin_email=request.POST.get('Email')
        obj.admin_gender=request.POST.get('gender')
        # obj.admin_photo=request.POST.get('Photo')
        myfile = request.FILES['Photo']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.admin_photo = myfile.name

        obj.number=request.POST.get('number')
        obj.admin_password=request.POST.get('Password')
        obj.admin_username=request.POST.get('User')
        obj.save()

    return render(request, 'coadmin/coadmin.html')
def view_adminn(request):
    obj=Coadmin.objects.all()
    context={
        'rr':obj
    }
    return render(request, 'coadmin/view_coadmin.html', context)


def delete(request, idd):
    obj = Coadmin.objects.get(admin_id=idd)
    obj.delete()
    ob = Login.objects.filter(u_id=idd, type="co_admin")
    ob.delete()
    return view_adminn(request)

def accept(request,idd):
    obj=Coadmin.objects.get(admin_id=idd)
    obj.admin_status='accepted'
    obj.save()
    ob = Login()
    ob.username = obj.admin_username
    ob.password = obj.admin_password
    ob.u_id = obj.admin_id
    ob.type = 'co_admin'
    ob.save()
    return view_adminn(request)