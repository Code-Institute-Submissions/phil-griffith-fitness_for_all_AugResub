# Generated by Django 3.2.3 on 2021-07-24 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20210724_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='expired_full_member',
            field=models.BooleanField(default=False),
        ),
    ]