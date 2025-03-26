from django.db import models
from coadmin.models import Coadmin

# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_duration = models.CharField(max_length=50)
    course = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'course'

class SelectCourse(models.Model):
    select_course_id = models.AutoField(primary_key=True)
    # course_id = models.IntegerField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    # coadmin_id = models.IntegerField()
    coadmin=models.ForeignKey(Coadmin,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'select_course'
