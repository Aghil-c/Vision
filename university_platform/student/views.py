from django.shortcuts import render
from student.models import Student
# Create your views here.
def viewstudents(request):
    obj=Student.objects.all()
    context={
        'hhh':obj
    }
    return render(request,'student/viewstudent.html',context)
def delete(request, idd):
    obj = Student.objects.get(student_id=idd)
    obj.delete()
    return viewstudents(request)
