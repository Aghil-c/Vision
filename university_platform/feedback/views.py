from django.shortcuts import render
from feedback.models import Feedback

# Create your views here.
def viewfeedback(request):
    obj=Feedback.objects.all()
    context={
        'f':obj
    }

    return render(request,'feedback/viewfeedback.html',context)