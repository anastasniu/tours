# Generated by Django 4.2.3 on 2023-11-05 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_alter_review_created_alter_review_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 18, 39, 10, 586465)),
        ),
        migrations.AlterField(
            model_name='review',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 18, 39, 10, 586465)),
        ),
    ]
