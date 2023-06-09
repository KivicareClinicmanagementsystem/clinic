# Generated by Django 4.1.7 on 2023-05-12 04:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kkarmapp', '0015_alter_appoinment_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='poston',
            field=models.DateField(default=datetime.date(2023, 5, 12)),
        ),
        migrations.CreateModel(
            name='PatientReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Report', models.FileField(upload_to='PatientReports/')),
                ('DoctorFeedback', models.TextField()),
                ('PatientFeedback', models.TextField()),
                ('report_date', models.DateField(auto_now=True)),
                ('Userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'PatientReports',
            },
        ),
    ]
