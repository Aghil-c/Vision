from django.db import models


# Create your models here.
class Calender(models.Model):
    calender_id = models.AutoField(primary_key=True)
    calender_date = models.DateField()
    calender_description = models.CharField(max_length=100)
    calender_time = models.TimeField()
    calender_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calender'

