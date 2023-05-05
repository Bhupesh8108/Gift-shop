from django.core.mail import send_mail
def send_reset_link(token,email):
    subject = "Password reset link"
    message = f"""Here is the link to reset you password Please follow 
    instructions to reset your password. Thank you and keep gifting you loved ones with giftwan.pythonanywhere.com
    https://giftwan.pythonanywhere.com/password-set/{token}"""
    sender = "info.giftwan@gmail.com"
    recipient = [email]
    send_mail(subject,message,sender,recipient)
    return True
