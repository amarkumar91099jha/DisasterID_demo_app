# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile, EmailVerification, BasicUserDetails, UserAddress
from .utils import sendEmail
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
import json

def email_auth(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        existing_user = UserProfile.objects.filter(email=email).exists()

        # Validate email
        if not existing_user:
            # Create a user profile
            user_profile, created = UserProfile.objects.get_or_create(email=email)
            
            # Create an email verification entry with a random OTP
            email_verification, created = EmailVerification.objects.get_or_create(user_profile=user_profile)
            email_verification.generate_otp()  # You need to implement this method in your model
            message= "Your otp for DisasterID creation is:"+email_verification.otp
            sendEmail(email_verification.id,message)
            # Redirect to OTP input page
            return redirect('otp_input', email_verification_id=email_verification.id)
        else:
            error_message = "Email already exists. Please use a different email."
            return render(request, 'DisasterID/email_auth.html', {'error_message': error_message})

    return render(request, 'DisasterID/email_auth.html')

def otp_input(request, email_verification_id, ):
    email_verification = EmailVerification.objects.get(id=email_verification_id)

    if request.method == 'POST':
        otp = request.POST.get('otp')

        # Validate OTP
        if email_verification.verify_otp(otp): 
            
            flag=False
            while not flag:
                temp=get_random_string(length=12, allowed_chars='0123456789')
                if not UserProfile.objects.filter(disaster_id=temp).exists():
                    email_verification.user_profile.disaster_id=temp
                    email_verification.user_profile.save()
                    flag=True
                username=email_verification.user_profile.disaster_id
                password=get_random_string(length=8, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*')          
                user = User.objects.create_user(username=username, password=password)
                message="UserName: "+username + "\n Password: "+password
                email_verification.user_profile.savePassword(password)
                sendEmail(email_verification_id,message)
            return redirect('user_details', email_verification_id=email_verification.id)
        else:
            messages.error(request, 'Invalid OTP. Please try again.')

    return render(request, 'DisasterID/otp_input.html', {'email_verification': email_verification})

def user_details(request, email_verification_id):
    email_verification = EmailVerification.objects.get(id=email_verification_id)
    user_profile = email_verification.user_profile

    if request.method == 'POST':
        # Collect basic user details
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        livelihood = request.POST.get('livelihood')
        # Add other fields as needed

        # Create or update BasicUserDetails
        basic_details, created = BasicUserDetails.objects.get_or_create(user_profile=user_profile)
        basic_details.name = name
        basic_details.age = age
        basic_details.gender = gender
        basic_details.livelihood = livelihood
        # Update other fields as needed
        basic_details.save()

        # Redirect to address input page
        return redirect('address_input', email_verification_id=email_verification.id)

    return render(request, 'DisasterID/user_details.html', {'email_verification': email_verification})

def address_input(request, email_verification_id):
    email_verification = EmailVerification.objects.get(id=email_verification_id)
    user_profile = email_verification.user_profile

    if request.method == 'POST':
        # Collect user address
        gramPanchayat = request.POST.get('gram_panchayat')
        ward_no = request.POST.get('ward_no')
        tehsil_or_block = request.POST.get('tehsil')
        pincode=request.POST.get('pincode')
        district = request.POST.get('district')
        state = request.POST.get('state')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        # Add other fields as needed

        # Create or update UserAddress
        user_address, created = UserAddress.objects.get_or_create(user_profile=user_profile)
        user_address.gramPanchayat=gramPanchayat
        user_address.ward_no=ward_no
        user_address.tehsil_or_block=tehsil_or_block
        user_address.pincode=pincode
        user_address.district=district
        user_address.state=state
        user_address.latitude=latitude
        user_address.longitude=longitude
        # Update other fields as needed
        user_address.save()
        
        messages.success(request, 'Profile created successfully!')
        return redirect('disasterID_card',email_verification_id=email_verification.id)

    return render(request, 'DisasterID/address_input.html', {'email_verification': email_verification})


def disasterID(request, email_verification_id):
    email_verification = EmailVerification.objects.get(id=email_verification_id)
    user_profile=email_verification.user_profile
    basic_user_details=BasicUserDetails.objects.get(user_profile_id=email_verification.user_profile)
    user_address=UserAddress.objects.get(user_profile_id=email_verification.user_profile)
    password=user_profile.password
    return render(request, "DisasterID/disasterID_Card.html",{
        "user_profile":user_profile,
        "email_verification": email_verification,
        "user_detail":basic_user_details,
        "user_address":user_address,
        "password":password
        })


def home(request):
    address=UserAddress.objects.all().values()
    addresses=json.dumps(list(address))
    return render(request, "base.html",{
        "address":addresses,
        
    })



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        user_profile=UserProfile.objects.get(disaster_id=username)
        if user is not None:
            login(request, user)
            email_verification=EmailVerification.objects.get(user_profile=user_profile)
            return redirect('profile-page', email_verification_id=email_verification.id)  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'DisasterID/login.html')

def formView(requests, email_verification_id):
    # email_verification = EmailVerification.objects.get(id=email_verification_id)
    return render(requests, "DisasterID/form_page.html",{
        # "email_id":email_verification,
    })