from django.core.mail import send_mail
import requests
from django import template

register = template.Library()

@register.filter(name='div')
def div(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return None
    
def send_reset_link(token,email):
    subject = "Password reset link"
    message = f"""Here is the link to reset you password Please follow instructions to
reset your password. Thank you and keep gifting you loved ones with giftwan
https://giftwan.pythonanywhere.com/password-set/{token}"""
    sender = "bishalpaudel1011@gmail.com"
    recipient = [email]
    # send_mail(subject,message,sender,recipient)
    return requests.post("https://api.mailgun.net/v3/sandbox5420a4199b14452a8bc7366190968f0a.mailgun.org/messages",
                  auth=("api", "79ecadcdeec0def5cfff4e08dab8f507-6b161b0a-17363858"),
		data={"from": "Giftwan <noreply@gmail.com>",
			"to": ["bhupeshdawadi1016@gmail.com"],
			"subject": subject,
			"text": message})

def send_order_mail(email,product,quantity,address,number,user):
    subject = "Order recieved"
    message =f'''
    Dear {user}, 
    We have received the order from you 
    email : {email},
    product_id:{product},
    quantity:{quantity},
    address:{address},
    number:{number},
    '''
    # sender = 'bishalpaudel1011@gmail.com'
    # recipient = [email,'bhupeshdawadi12345@gmail.com']
    # send_mail(subject,message,sender,recipient)



    requests.post("https://api.mailgun.net/v3/sandbox5420a4199b14452a8bc7366190968f0a.mailgun.org/messages",
                  auth=("api", "79ecadcdeec0def5cfff4e08dab8f507-6b161b0a-17363858"),
		data={"from": "Giftwan <noreply.giftwan@gmail.com>",
			"to": ["bhupeshdawadi1016@gmail.com"],
			"subject": subject,
			"text": message})
