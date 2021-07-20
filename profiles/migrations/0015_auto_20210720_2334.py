# Generated by Django 3.2.3 on 2021-07-20 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_userprofile_days_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='days_added',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='membership_level_selected',
            field=models.IntegerField(default=0),
        ),
    ]
