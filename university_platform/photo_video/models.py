from django.db import models
from student.models import Student
from faculty.models import Faculty


# Create your models here.
class PhotoVideo(models.Model):
    pv_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    pv_date = models.DateField()
    pv_time = models.TimeField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    #student_id = models.IntegerField()
    pv = models.CharField(max_length=300)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    #faculty_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'photo_video'

