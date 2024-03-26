from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from DisasterID.models import UserProfile
# Create your models here.


class FamilyMember(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    OCCUPATION_CHOICES = (
        ('Student', 'Student'),
        ('Employed', 'Employed'),
        ('Unemployed', 'Unemployed'),
    )
    STATUS_CHOICES = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    )
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)






class Shelter_Details(models.Model):
    # Choices for house type
    HOUSE_TYPE_CHOICES = [
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Bungalow', 'Bungalow'),
        ('Cottage', 'Cottage'),
        ('Other', 'Other'),
    ]
    
    # Choices for extent of house damage
    HOUSE_DAMAGE_CHOICES = [
        ('Self Owned', 'Self Owned'),
        ('Govt. Owned', 'Govt. Owned'),
        ('Rented', 'Rented'),
    ]

    # Choices for availability of toilets
    TOILET_CHOICES = [
        (True, 'Yes'),
        (False, 'No'),
    ]

    # Choices for drinking water source
    DRINKING_WATER_CHOICES = [
        (True, 'Available'),
        (False, 'Not available'),
    ]

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    house_type = models.CharField(max_length=100, choices=HOUSE_TYPE_CHOICES)
    room_numbers = models.IntegerField()
    availability_of_toilets = models.BooleanField(choices=TOILET_CHOICES)
    drinking_water_source = models.BooleanField(choices=DRINKING_WATER_CHOICES)
    ownership_type = models.CharField(max_length=50, choices=HOUSE_DAMAGE_CHOICES)
