# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('email-auth/', views.email_auth, name='email_auth'),
    path('otp-input/<int:email_verification_id>/', views.otp_input, name='otp_input'),
    path('user-details/<int:email_verification_id>/', views.user_details, name='user_details'),
    path('address-input/<int:email_verification_id>/', views.address_input, name='address_input'),
    path('disasterID-card/<int:email_verification_id>/', views.disasterID, name='disasterID_card'),
    path('login/', views.login_view, name='login'),
    path('form-page/<int:email_verification_id>/', views.formView, name='form-page'),
    # Other paths go here
]
