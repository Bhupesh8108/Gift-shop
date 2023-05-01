from django.shortcuts import render
from .models import item,categories,wishlist
from django.views import View
from .forms import CustomerRegistrationForm,authentication
from django.contrib import messages
from django.contrib.auth.models import User



def home(request):
 products = item.objects.all()
 return render(request, 'app/home.html',{"products":products,"categories":categories})





def product_detail(request,id):
 prod = item.objects.filter(id=id).first()
 user = request.user
 try:
  product_id = request.GET.get('product_id')
  product = item.objects.get(id = product_id)
  if wishlist.objects.filter(product=product).exists():
   messages.warning(request,"Product is already in cart")
  else:
    wishlist(user=user, product=product,quantity=1).save()
    messages.success(request,'Product added to cart') 
 except:
  pass
 return render(request, 'app/productdetail.html',{'prod':prod})





def add_to_cart(request):
  user = request.user
  cart_items = wishlist.objects.filter(user=user)
  try:
   cart_id = request.GET.get('cart_id')
   wishlist.objects.filter(id=cart_id).delete()
  except:
   pass
  price = 0
  for cart_item in cart_items:
    price += int(cart_item.product.price) * int(cart_item.quantity)
  return render(request, 'app/addtocart.html',{'cart_items': cart_items,'price': float(price,),'total':float(price+50)})








def buy_now(request):
 return render(request, 'app/buynow.html')





def profile(request):
 return render(request, 'app/profile.html')





def address(request):
 return render(request, 'app/address.html')






def orders(request):
 return render(request, 'app/orders.html')





def change_password(request):
 return render(request, 'app/changepassword.html')




def mobile(request):
 return render(request, 'app/mobile.html')





class customerregistration(View):
 def get (self, request):
  form = CustomerRegistrationForm()
  return render(request, 'app/customerregistration.html', {'form': form})
 

 def post(self, request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():    
    user = form.save(commit=False)
    email = form.cleaned_data['email']
    if "@gmail.com" not in email and len(email)<13:
     messages.warning(request,'invalid email address')
    else:
      if User.objects.filter(email = email).exists():
       messages.warning(request,"Email already used")
      else:
        user.email = email
        user.save()
        messages.success(request,'User registered successfully')
  return render(request, 'app/customerregistration.html', {'form': form})



def checkout(request):
 return render(request, 'app/checkout.html')
