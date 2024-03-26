import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .models import EmailVerification

def sendEmail(id, message):
    email_obj = EmailVerification.objects.get(id=id)
    otp = str(email_obj.otp)
    from_mail = 'amarkumar555999abc@gmail.com'
    from_password = 'lcqbevgbkzfqomok'
    to_mail = email_obj.user_profile.email
    smtp_server = "smtp.gmail.com"
    smtp_port = 465

    # Define the function for sending the email
    def send_email(from_mail, from_password, to_mail, message):
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = from_mail
        msg['To'] = to_mail
        msg['Subject'] = 'Email Verification for DisasterID: OTP'

        # Attach HTML message
        msg.attach(MIMEText(message, 'html'))

        # Connect to SMTP server
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(from_mail, from_password)
            # Send the email
            server.send_message(msg)

    # Call the function to send the email
    send_email(from_mail, from_password, to_mail, message)
