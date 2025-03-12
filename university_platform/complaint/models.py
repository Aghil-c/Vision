from django.db import models
from coadmin.models import Coadmin
from faculty.models import Faculty

# Create your models here.
class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint_date = models.DateField()
    complaint_time = models.TimeField()
    complaint = models.CharField(max_length=100)
    complaint_replay = models.CharField(max_length=100)
    #faculty_id = models.IntegerField()
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    # admin_id = models.IntegerField()
    admin=models.ForeignKey(Coadmin,on_delete=models.CASCADE)
    complaint_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'complaint'


