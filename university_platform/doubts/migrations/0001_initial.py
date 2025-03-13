# Generated by Django 3.2.25 on 2025-03-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doubt',
            fields=[
                ('doubt_id', models.AutoField(primary_key=True, serialize=False)),
                ('doubt', models.CharField(max_length=100)),
                ('doubt_date', models.DateField()),
                ('doubt_time', models.TimeField()),
                ('doubt_replayl', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'doubt',
                'managed': False,
            },
        ),
    ]
