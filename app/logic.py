from email.message import EmailMessage
import smtplib , ssl, random
from django.core.mail import send_mail
# def send_email(request, product,user,email,quantity,address,phone_number):
#     password = 'fokaauhqkeakxngp'
#     sender = 'info.giftwan@gmail.com'
#     # reveiver = ['binitshrestha832@gmail.com','poudelbishal69@gmail.com']
#     reveiver = ['bhupeshdawadi12345@gmail.com']
#     subject = 'New order recieved'
#     body = f'''
#     product : {product}
#     quantity : {quantity}
#     address : {address}
#     phone_number : {phone_number}
#     user_email : {email}
#     user_name ; {user}
#     '''
#     print(body)
#     em = EmailMessage()
#     em['From'] = sender
#     em['Subject'] = subject
#     em['To'] = sender
#     em.set_content(body)
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
#         smtp.login(sender,password)
#         smtp.sendmail(sender,reveiver,em.as_string())


def send_reset_link(token,email):
    subject = "Password reset link"
    message = f"https://giftwan.pythonanywhere.com/password-set/{token}"
    sender = "info.giftwan@gmail.com"
    recipient = [email]
    send_mail(subject,message,sender,recipient)
    return True
