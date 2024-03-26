from django import forms
from .models import FamilyMember,Shelter_Details

class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = ['user_profile', 'name', 'age', 'gender', 'occupation', 'status']
        widgets = {
            'gender': forms.Select(choices=FamilyMember.GENDER_CHOICES),
            'occupation': forms.Select(choices=FamilyMember.OCCUPATION_CHOICES),
            'status': forms.Select(choices=FamilyMember.STATUS_CHOICES),
        }



class ShelterDetailsForm(forms.ModelForm):
    class Meta:
        model = Shelter_Details
        fields = ['user_profile','house_type', 'room_numbers', 'availability_of_toilets', 'drinking_water_source', 'ownership_type']
        labels = {
            'house_type': 'House Type',
            'room_numbers': 'Room Numbers',
            'availability_of_toilets': 'Availability of Toilets',
            'drinking_water_source': 'Drinking Water Source',
            'ownership_type': 'Ownership Types',
        }
        widgets = {
            'house_type': forms.Select(choices=Shelter_Details.HOUSE_TYPE_CHOICES),
            'room_numbers': forms.NumberInput(attrs={'min': 0}),
            'availability_of_toilets': forms.Select(choices=Shelter_Details.TOILET_CHOICES),
            'drinking_water_source': forms.Select(choices=Shelter_Details.DRINKING_WATER_CHOICES),
            'ownership_type': forms.Select(choices=Shelter_Details.HOUSE_DAMAGE_CHOICES),
        }

