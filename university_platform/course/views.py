from django.shortcuts import render
from course.models import Course,SelectCourse
from faculty.models import Faculty

# Create your views here.
def course(request):
    if request.method=='POST':
        obj=Course()
        obj.course=request.POST.get('course')
        obj.course_duration=request.POST.get('duration')
        obj.save()



    return render(request,'course/course.html')


def viewcourse(request):
    ss = request.session['u_id']
    ab=Faculty.objects.get(faculty_id=ss)
    obj=SelectCourse.objects.filter(coadmin_id=ab.admin_id)
    print(obj)
    context={
        'cc':obj
    }

    return render(request, 'course/seletcourse.html', context)

def delete_course(request):
    obj=Course.objects.all()
    context={
        'cc':obj
    }
    return render(request,'course/delete_course.html',context)


def delete(request,idd):
    obj = Course.objects.get(course_id=idd)
    obj.delete()
    return delete_course (request)


def select_course(request):
    obj=Course.objects.all()
    context={
        'ccc':obj
    }
    return render(request, 'course/seletcourse.html', context)


def deletes_course(request):
    ss = request.session['u_id']
    obj=SelectCourse.objects.filter(coadmin_id=ss)
    context={
        'ccc':obj
    }
    return render(request, 'course/delete_selectcourse.html', context)

def deletes(request,idd):
    obj = SelectCourse.objects.get(select_course_id=idd)
    obj.delete()
    return deletes_course(request)




def selectcoursebyco(request,idd):
    ss=request.session['u_id']
    obj=SelectCourse()
    obj.course_id=idd
    obj.coadmin_id=ss
    obj.save()
    return select_course(request)

def view_selected_course(request):
    obj=Course.objects.all()
    context={
        'ccc':obj
    }

    return render(request, 'course/seletcourse.html', context)