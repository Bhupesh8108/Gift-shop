from .models import wishlist
from django.contrib.auth.models import Group
from datetime import datetime,timedelta
def common_data(request):
    if request.user.is_authenticated:
        group_user = request.user.groups.filter(name='seller')
        cart_list = wishlist.objects.filter(user=request.user)
        nocart = len(cart_list)
    else:
        nocart = 0
        group_user = None
    return{'nocart':nocart,"seller":group_user}

def delivery_time(request):
    utc_time = datetime.today()
    nepal_time = utc_time + timedelta(seconds=5*60*60+45*60)
    if int(nepal_time.strftime('%H')) < 16:
        delivery_time = nepal_time.strftime('%b-%d')
    else:
        nepal_time = utc_time + timedelta(days=1)
        delivery_time = nepal_time.strftime('%b-%d')
    return {'delivery_time':delivery_time}

   
