from django.db import models
from student.models import Student

# Create your models here.
class Activities(models.Model):
    activities_id = models.AutoField(primary_key=True)
    activities = models.CharField(max_length=100)
    faculty_id = models.IntegerField()
    activities_name = models.CharField(max_length=45)
   # student_id = models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    activity_date = models.CharField(max_length=45, blank=True, null=True)
    activity_time = models.CharField(max_length=45, blank=True, null=True)
    activity_response = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activities'

