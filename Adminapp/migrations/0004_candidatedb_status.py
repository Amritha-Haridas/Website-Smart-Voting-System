# Generated by Django 4.1.1 on 2022-10-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0003_candidatedb_password_candidatedb_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatedb',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
