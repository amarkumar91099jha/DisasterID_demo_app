from django.urls import path
from userProfile.views import userProfile, add_family_member, edit_family_member, add_shelter_details_view, Ressolv


urlpatterns=[
    path("/profile/<int:email_verification_id>/", userProfile, name='profile-page'),
    path("/add-members/<int:user_profile_id>/", add_family_member, name="add-members"),
    path("/edit-members-details/<int:member_id>/", edit_family_member, name="edit-members-details"),
    path("/add-shelterdetails/<int:user_profile_id>/", add_shelter_details_view, name="add-shelterdetails"),
    path("/ressolv", Ressolv, name="ressolv"),


]