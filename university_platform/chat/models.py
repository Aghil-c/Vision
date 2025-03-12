from django.db import models

# Create your models here.
class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    chat_date = models.DateField()
    chat_time = models.TimeField()
    student_id = models.IntegerField()
    faculty_id = models.IntegerField()
    chat = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'chat'

