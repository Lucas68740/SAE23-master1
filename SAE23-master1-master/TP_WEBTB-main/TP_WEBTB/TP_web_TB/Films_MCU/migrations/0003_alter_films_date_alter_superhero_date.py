# Generated by Django 4.0.5 on 2022-06-13 19:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Films_MCU', '0002_categoriesfilms_alter_films_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 19, 36, 27, 69172, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 19, 36, 27, 45243, tzinfo=utc)),
        ),
    ]
