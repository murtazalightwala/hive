# Generated by Django 3.2.4 on 2021-07-03 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
        migrations.AddField(
            model_name='patient',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
