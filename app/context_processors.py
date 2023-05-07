from .models import wishlist
from datetime import datetime,timedelta
def common_data(request):
    if request.user.is_authenticated:
        cart_list = wishlist.objects.filter(user=request.user)
        nocart = len(cart_list)
    else:
        nocart = 0
    return{'nocart':nocart}

def delivery_time(request):
    utc_time = datetime.today()
    nepal_time = utc_time + timedelta(seconds=5*60*60+45*60)
    if int(nepal_time.strftime('%H')) < 16:
        delivery_time = nepal_time.strftime('%b-%d')
    else:
        nepal_time = utc_time + timedelta(days=1)
        delivery_time = nepal_time.strftime('%b-%d')
    return {'delivery_time':delivery_time}