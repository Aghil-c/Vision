from django.db import models
from coadmin.models import Coadmin

# Create your models here.
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    notification_time = models.TimeField()
    notification_date = models.DateField()
    notification = models.CharField(max_length=300)
    admin = models.ForeignKey(Coadmin, on_delete=models.CASCADE)
    #admin_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notification'


class AdminNotification(models.Model):
    admin_notification_id = models.AutoField(primary_key=True)
    admin_notificationdate = models.DateField()
    admin_notification_time = models.TimeField()
    admin_notification = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'admin_notification'

