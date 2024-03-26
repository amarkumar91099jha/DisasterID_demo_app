from django.shortcuts import render, redirect, get_object_or_404
from DisasterID.models import UserProfile, EmailVerification, BasicUserDetails, UserAddress
from .forms import FamilyMemberForm, ShelterDetailsForm
from .models import FamilyMember, Shelter_Details


# Create your views here.


def userProfile(requests, email_verification_id):
    email_verification = EmailVerification.objects.get(id=email_verification_id)
    basicdetails=BasicUserDetails.objects.get(user_profile_id=email_verification.user_profile.id)
    familyMembers=FamilyMember.objects.filter(user_profile_id=email_verification.user_profile.id)
    shelterdetails=Shelter_Details.objects.filter(user_profile_id=email_verification.user_profile.id)
    return render(requests, "userProfile/home.html", {
        "user_profile": email_verification.user_profile,
        "basicdetails":basicdetails,
        "familymembers":familyMembers,
        "shelterdetails":shelterdetails
    })


def add_family_member(request, user_profile_id):
    user_profile = UserProfile.objects.get(pk=user_profile_id)  # Replace with your logic to retrieve the user_profile object
    email_verification=EmailVerification.objects.get(user_profile_id=user_profile_id)
    if request.method == 'POST':
        form = FamilyMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile-page',email_verification.id )
    else:
        # Assuming you have retrieved the user_profile object based on the current user or some other criteria
        # Replace with your logic to retrieve the user_profile object

        # Pass the user_profile as initial data to the form
        form = FamilyMemberForm(initial={'user_profile': user_profile})

    return render(request, 'userProfile/addMembers.html', {'form': form})


def edit_family_member(request, member_id):
    family_member = FamilyMember.objects.get(pk=member_id)
    email_verification=EmailVerification.objects.get(user_profile_id=family_member.user_profile.id)

    if request.method == 'POST':
        form = FamilyMemberForm(request.POST, instance=family_member)
        if form.is_valid():
            form.save()
            return redirect('profile-page',email_verification.id )
    else:
        form = FamilyMemberForm(instance=family_member)

    return render(request, 'userProfile/edit_family_member.html', {'form': form})


# def shelter_details_view(request):
#     if request.method == 'POST':
#         form = ShelterDetailsForm(request.POST)
#         if form.is_valid():
#             # Save the form data to the database
#             shelter_details = form.save(commit=False)
#             shelter_details.user_profile = request.user.profile  # Assuming you have user profiles
#             shelter_details.save()
#             # Redirect to a success page or render another template
#     else:
#         form = ShelterDetailsForm()
#     return render(request, 'shelter_details.html', {'form': form})

def add_shelter_details_view(request, user_profile_id):
    user_profile = UserProfile.objects.get(pk=user_profile_id)  # Replace with your logic to retrieve the user_profile object
    email_verification=EmailVerification.objects.get(user_profile_id=user_profile_id)
    if request.method == 'POST':
        form = ShelterDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile-page',email_verification.id )
    else:
        # Assuming you have retrieved the user_profile object based on the current user or some other criteria
        # Replace with your logic to retrieve the user_profile object

        # Pass the user_profile as initial data to the form
        form = ShelterDetailsForm(initial={'user_profile': user_profile})

    return render(request, 'userProfile/addshelterdetails.html', {'form': form})


def Ressolv(request):
    return render(request,"userProfile/map.html")