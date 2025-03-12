from django.db import models
from course.models import Course
from coadmin.models import Coadmin
from faculty.models import Faculty


# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_age = models.IntegerField()
    student_gender = models.CharField(max_length=50)
    student_phone = models.IntegerField()
    student_email = models.CharField(max_length=100)
    course=models.ForeignKey(Faculty,on_delete=models.CASCADE)
   # course_id = models.CharField(max_length=100)
    student_photo = models.CharField(max_length=500)
    student_username = models.CharField(max_length=100)
    student_password = models.IntegerField()
    admin = models.ForeignKey(Coadmin, on_delete=models.CASCADE)
    #admin_id = models.IntegerField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
   # faculty_id = models.IntegerField()
    course = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'student'

