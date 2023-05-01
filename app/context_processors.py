from .models import wishlist
def common_data(request):
    if request.user.is_authenticated:
        cart_list = wishlist.objects.filter(user=request.user)
        nocart = len(cart_list)
    else:
        nocart = 0
    return{'nocart':nocart}

