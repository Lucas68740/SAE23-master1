# Generated by Django 4.0.5 on 2022-06-13 19:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Films_MCU', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoriesfilms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=45, null=True)),
                ('descriptif', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'CategoriesFilms',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='films',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 19, 29, 44, 556355, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 19, 29, 44, 530514, tzinfo=utc)),
        ),
    ]