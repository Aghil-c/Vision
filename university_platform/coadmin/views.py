from django.shortcuts import render
from coadmin.models import Coadmin

# Create your views here.
def adminn(request):
    if request.method=='POST':
        obj=Coadmin()
        obj.admin_college=request.POST.get('college')
        obj.admin_email=request.POST.get('Email')
        obj.admin_gender=request.POST.get('gender')
        obj.admin_photo=request.POST.get('Photo')
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
    return view_adminn(request)

def accept(request,idd):
    obj=Coadmin.objects.get(admin_id=idd)
    obj.admin_status='accepted'
    obj.save()
    return view_adminn(request)