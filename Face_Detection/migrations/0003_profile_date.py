# Generated by Django 3.2.15 on 2022-10-13 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Face_Detection', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date',
            field=models.DateField(default='2000-12-02'),
        ),
    ]
