# Generated by Django 4.1.1 on 2024-03-08 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DisasterID', '0007_userprofile_password'),
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShelterDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_type', models.CharField(choices=[('Apartment', 'Apartment'), ('House', 'House'), ('Bungalow', 'Bungalow'), ('Cottage', 'Cottage'), ('Other', 'Other')], max_length=100)),
                ('room_numbers', models.IntegerField()),
                ('damage_to_toilets', models.BooleanField()),
                ('damage_to_drinking_water_source', models.BooleanField()),
                ('extent_of_house_damage', models.CharField(choices=[('Minor', 'Minor'), ('Moderate', 'Moderate'), ('Severe', 'Severe')], max_length=50)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DisasterID.userprofile')),
            ],
        ),
    ]
