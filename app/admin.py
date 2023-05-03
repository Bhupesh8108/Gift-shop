from django.contrib import admin
from .models import item,wishlist,customer,order,search
admin.site.register(item)
admin.site.register(wishlist)
admin.site.register(customer)
admin.site.register(order)
admin.site.register(search)

# Register your models here.
