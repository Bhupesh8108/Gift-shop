from django.contrib import admin
from .models import item,wishlist,customer,order,search,forget_password
admin.site.register(item)
admin.site.register(wishlist)
admin.site.register(customer)
admin.site.register(order)
admin.site.register(search)
admin.site.register(forget_password)

# Register your models here.
