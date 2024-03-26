# models.py

from django.db import models
from django.utils.crypto import get_random_string
from django.core.validators import MinValueValidator,MaxValueValidator

class UserProfile(models.Model):
    email = models.EmailField(unique=True, null=True)
    disaster_id = models.CharField(max_length=12, unique=True, null=True)
    password=models.CharField(max_length=18, null=True)
    def savePassword(self,password):
        self.password=password
        self.save()


class EmailVerification(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)

    def generate_otp(self):
        self.otp = get_random_string(length=6, allowed_chars='0123456789')
        self.save()

    def verify_otp(self, entered_otp):
        return self.otp == entered_otp

class BasicUserDetails(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    age=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(120)], null=True)
    gender=models.CharField(max_length=20, null=True)
    livelihood=models.CharField(max_length=50, null=True)

    # Add other fields for basic user details

class UserAddress(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # address = models.TextField()
    gramPanchayat=models.CharField(max_length=50,null=True)
    ward_no=models.CharField(max_length=20, null=True)
    tehsil_or_block=models.CharField(max_length=50,null=True)
    pincode=models.IntegerField(null=True)
    district=models.CharField(max_length=50, null=True)
    state=models.CharField(max_length=50, null=True)
    latitude=models.CharField(max_length=20, null=True)
    longitude=models.CharField(max_length=20, null=True)
    # Add other fields for user address
