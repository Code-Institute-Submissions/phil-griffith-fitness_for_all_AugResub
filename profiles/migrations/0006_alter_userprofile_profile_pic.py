# Generated by Django 3.2.3 on 2021-06-06 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='{{ MEDIA_URL }}noimage.png', null=True, upload_to='profile_pics'),
        ),
    ]
