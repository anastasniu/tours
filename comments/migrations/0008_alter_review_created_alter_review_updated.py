# Generated by Django 4.2.3 on 2023-11-05 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0007_alter_review_created_alter_review_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 19, 19, 30, 433247)),
        ),
        migrations.AlterField(
            model_name='review',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 19, 19, 30, 433247)),
        ),
    ]
