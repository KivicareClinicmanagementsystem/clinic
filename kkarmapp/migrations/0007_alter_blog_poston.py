# Generated by Django 4.0 on 2023-03-21 05:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kkarmapp', '0006_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='poston',
            field=models.DateField(default=datetime.date(2023, 3, 20)),
        ),
    ]