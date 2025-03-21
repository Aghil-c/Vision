# Generated by Django 3.2.25 on 2025-03-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('activities_id', models.AutoField(primary_key=True, serialize=False)),
                ('activities', models.CharField(max_length=100)),
                ('faculty_id', models.IntegerField()),
                ('activities_name', models.CharField(max_length=45)),
                ('activity_date', models.CharField(blank=True, max_length=45, null=True)),
                ('activity_time', models.CharField(blank=True, max_length=45, null=True)),
                ('activity_response', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'activities',
                'managed': False,
            },
        ),
    ]
