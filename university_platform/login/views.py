from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect

# Create your views here.
def login(request):
    if request.method =='POST':
        uname=request.POST.get("un")
        passwd=request.POST.get("ps")
        obj = Login.objects.filter(username=uname,password=passwd)
        tp = ""
        for ob in obj:
            tp=ob.type
            uid=ob.u_id
            if tp == "co_admin":
                request.session['u_id'] =uid
                return HttpResponseRedirect('/temp/post_co_admin/')
            elif tp == "faculty":
                request.session['u_id']= uid
                return HttpResponseRedirect('/temp/post_staff/')
            elif tp == "admin":
                request.session['u_id']= uid
                return HttpResponseRedirect('/temp/post_admintemp/')

            else:
                objlist="Username name or Password incorrect ... please try again"
                context={
                    'msg':objlist
                }
                return render(request,'login/login.html',context)


    return render (request,'login/login.html')