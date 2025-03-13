# Generated by Django 3.2.25 on 2025-03-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('faculty_id', models.AutoField(primary_key=True, serialize=False)),
                ('faculty_username', models.CharField(max_length=100)),
                ('faculty_password', models.IntegerField()),
                ('faculty_email', models.CharField(max_length=100)),
                ('faculty_gender', models.CharField(max_length=50)),
                ('faculty_photo', models.CharField(max_length=300)),
                ('faculty_phonel', models.CharField(max_length=45)),
                ('faculty_status', models.CharField(max_length=45)),
                ('faculty_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'faculty',
                'managed': False,
            },
        ),
    ]
