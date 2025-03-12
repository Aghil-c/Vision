from django.shortcuts import render


# Create your views here.
def admintemp(request):
    return render(request,'temp/admintemp.html')
def co_admin(request):
    return render(request,'temp/co admin.html')
def home(request):
    return render(request,'temp/homee.html')
def staff(request):
    return render(request,'temp/staff.html')
