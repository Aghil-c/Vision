from django.db import models

# Create your models here.
class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=50)
    faculty_id = models.IntegerField()
    student_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'group'
