from django.db import models
from coadmin.models import Coadmin



# Create your models here.
class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    faculty_username = models.CharField(max_length=100)
    faculty_password = models.IntegerField()
    faculty_email = models.CharField(max_length=100)
    faculty_gender = models.CharField(max_length=50)
    faculty_photo = models.CharField(max_length=300)
    admin = models.ForeignKey(Coadmin, on_delete=models.CASCADE)
   # admin_id = models.IntegerField()
    faculty_phonel = models.CharField(max_length=45)
    faculty_status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'faculty'
