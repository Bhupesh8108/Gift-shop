from django.shortcuts import render
from .models import item,categories
from django.views import View
from .forms import CustomerRegistrationForm,authentication
from django.contrib import messages
from django.contrib.auth.models import User



def home(request):
 products = item.objects.all()
 return render(request, 'app/home.html',{"products":products,"categories":categories})





def product_detail(request,id):
 prod = item.objects.filter(id=id).first()
 return render(request, 'app/productdetail.html',{'prod':prod})





def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('product_id')
#  product = item.objects.get(id = product_id)
#  print(product,user,product_id)
#  cart(user_id=user, Product=product_id,Quantity=1).save()
 return render(request, 'app/addtocart.html')








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
