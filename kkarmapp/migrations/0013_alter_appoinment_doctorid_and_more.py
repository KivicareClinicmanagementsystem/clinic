# Generated by Django 4.1.7 on 2023-04-25 04:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kkarmapp', '0012_alter_treatments_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment',
            name='doctorid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kkarmapp.doctor'),
        ),
        migrations.AlterField(
            model_name='appoinment',
            name='treatmentid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kkarmapp.treatments'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='poston',
            field=models.DateField(default=datetime.date(2023, 4, 25)),
        ),
    ]
