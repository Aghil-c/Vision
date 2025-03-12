from django.db import models
from student.models import Student


# Create your models here.
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    faculty_time = models.TimeField()
    faculty_date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
   # student_id = models.IntegerField()
    feedbackl = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'feedback'
