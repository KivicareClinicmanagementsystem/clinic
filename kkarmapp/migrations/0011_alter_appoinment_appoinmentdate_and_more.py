# Generated by Django 4.1.7 on 2023-04-18 12:01

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('kkarmapp', '0010_appoinment_alter_blog_poston'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment',
            name='Appoinmentdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appoinment',
            name='Appoinmenttime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='appoinment',
            name='Dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appoinment',
            name='address',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='appoinment',
            name='phoneno',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='poston',
            field=models.DateField(default=datetime.date(2023, 4, 18)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='description',
            field=tinymce.models.HTMLField(default=''),
        ),
    ]