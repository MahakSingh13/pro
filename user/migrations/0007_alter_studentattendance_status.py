# Generated by Django 5.0.6 on 2024-07-13 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_studentattendance_sclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentattendance',
            name='status',
            field=models.CharField(max_length=15),
        ),
    ]
