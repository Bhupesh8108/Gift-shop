from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from .models import item,categories,wishlist
from django.views import View
from .forms import CustomerRegistrationForm,authentication,password_change
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.views import LoginView,PasswordChangeView
from ipware import get_client_ip 
from ip2geotools.databases.noncommercial import DbIpCity






def home(request):
 products = item.objects.all()
 return render(request, 'app/home.html',{"products":products,"categories":categories})





def product_detail(request,id):
 prod = item.objects.filter(id=id).first()
 products = item.objects.all()
 user = request.user
 ip,routable = get_client_ip(request)
 print(ip)
 if ip is None:
  ip = '0.0.0.0'

 try:
  response = DbIpCity.get(ip,api_key="free")
 except:
  response = None
 print(response)
 try:
  product_id = request.GET.get('product_id')
  product = item.objects.get(id = product_id)
  if wishlist.objects.filter(product=product,user=request.user).exists():
   
   messages.warning(request,"Product is already in cart")
  else:
    wishlist(user=user, product=product,quantity=1).save()
    messages.success(request,'Product added to cart') 
 except:
  pass
 return render(request, 'app/productdetail.html',{'prod':prod,"products":products})








def login(request):
    pid = request.GET.get('product_id')
    if pid:
      return LoginView.as_view(template_name='app/login.html', authentication_form=authentication,next_page= f'/product-detail/{pid}')(request)
    else:
      return LoginView.as_view(template_name='app/login.html', authentication_form=authentication,next_page = '/')(request)
     








def update_price(request):
  user = request.user
  cart_items = wishlist.objects.filter(user=user)
  price = 0
  for cart_item in cart_items:
    price += int(cart_item.product.price) * int(cart_item.quantity)
  return price,cart_items



def cart(request):
  try:
   cart_id = request.GET.get('cart_id')
   wishlist.objects.filter(id=cart_id).delete()
  except:
   pass
  price,cart_items =update_price(request)
  return render(request, 'app/addtocart.html',{'cart_items': cart_items,'price': float(price),'total':float(price+50)})



def pluscart(request):
  if request.method == 'GET':
   pid = request.GET.get('produc_id')
   if pid:
    items = get_object_or_404(wishlist,product=pid,user=request.user)
    items.quantity += 1
    items.save()
    price,cart_items = update_price(request)
    data = {'quantity':items.quantity,
            'price':price,
            'total':price+50}
    return JsonResponse(data)
   


def minuscart(request):
 if request.method == 'GET':
   pid = request.GET.get('produc_id')
   if pid:
    items = get_object_or_404(wishlist,product=pid,user=request.user)
    items.quantity -= 1
    items.save()
    if items.quantity<=0:
     wishlist.objects.filter(product=pid,user=request.user).delete()
     

    price,cart_items= update_price(request)
    data = {'quantity':items.quantity,
            'price':price,
            'total':price+50,
            }
    return JsonResponse(data)
  

def removecart(request):
 if request.method == 'GET':
   pid = request.GET.get('produc_id')
   if pid:
    items = get_object_or_404(wishlist,product=pid,user=request.user)
    if items.quantity<=0:
     wishlist.objects.filter(product=pid,user=request.user).delete()

    price,_ = update_price(request)
    data = {'quantity':items.quantity,
            'price':price,
            'total':price+50}
    return JsonResponse(data)






def buy_now(request):
 return render(request, 'app/buynow.html')





def profile(request):
 return render(request, 'app/profile.html')





def address(request):
 return render(request, 'app/address.html')






def orders(request):
 return render(request, 'app/orders.html')








def change_password(request):
  return PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=password_change,success_url='/')(request)
 




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
