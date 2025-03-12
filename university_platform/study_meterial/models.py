from django.db import models
from faculty.models import Faculty

# Create your models here.
class StudyMaterial(models.Model):
    study_id = models.AutoField(primary_key=True)
    study_date = models.DateField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
   # faculty_id = models.IntegerField()
    study_material = models.CharField(max_length=300)
    study_time = models.TimeField()
    study_materialdes = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'study_material'

