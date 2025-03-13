from django.db import models

# Create your models here.
class Coadmin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_username = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=100)
    admin_email = models.CharField(max_length=100)
    admin_gender = models.CharField(max_length=50)
    admin_photo = models.CharField(max_length=300)
    admin_college = models.CharField(max_length=45)
    number = models.CharField(max_length=45)
    admin_status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'coadmin'


