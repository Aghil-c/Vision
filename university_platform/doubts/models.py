from django.db import models
from student.models import Student
from faculty.models import Faculty


# Create your models here.
class Doubt(models.Model):
    doubt_id = models.AutoField(primary_key=True)
    doubt = models.CharField(max_length=100)
    student =models.ForeignKey(Student,on_delete=models.CASCADE)
    #student_id = models.IntegerField()
    doubt_date = models.DateField()
    doubt_time = models.TimeField()
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    #faculty_id = models.IntegerField()
    doubt_replayl = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'doubt'
