# Generated by Django 5.0.1 on 2024-02-06 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DisasterID', '0005_alter_userprofile_disaster_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
    ]