# Generated by Django 5.0.1 on 2024-02-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DisasterID', '0003_remove_useraddress_address_useraddress_district_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='disaster_id',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
