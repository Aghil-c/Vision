# Generated by Django 3.2.25 on 2025-03-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coadmin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_username', models.CharField(max_length=100)),
                ('admin_password', models.CharField(max_length=100)),
                ('admin_email', models.CharField(max_length=100)),
                ('admin_gender', models.CharField(max_length=50)),
                ('admin_photo', models.CharField(max_length=300)),
                ('admin_college', models.CharField(max_length=45)),
                ('number', models.CharField(max_length=45)),
                ('admin_status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'coadmin',
                'managed': False,
            },
        ),
    ]
