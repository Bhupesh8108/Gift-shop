from django.core.mail import send_mail
def send_reset_link(token,email):
    subject = "Password reset link"
    message = f"""Here is the link to reset you password Please follow 
    instructions to reset your password. Thank you and keep gifting you loved ones with giftwan
   https://giftwan.pythonanywhere.com/password-set/{token}"""
    sender = "info.giftwan@gmail.com"
    recipient = [email]
    send_mail(subject,message,sender,recipient)
    return True

def send_order_mail(email,product,quantity,address,number,user):
    subject = "Order recieved"
    message =f'''
    Dear {user}, 
    We have received the order from you 
    email : {email},
    product:{product},
    quantity:{quantity},
    address:{address},
    number:{number},
    '''
    sender = 'noreply.giftwan@gmail.com'
    recipient = [email,'bhupeshdawadi12345@gmail.com']
    send_mail(subject,message,sender,recipient)
