# Generated by Django 3.2.25 on 2025-03-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('faculty_time', models.TimeField()),
                ('faculty_date', models.DateField()),
                ('feedbackl', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'feedback',
                'managed': False,
            },
        ),
    ]
