from django.shortcuts import render
from .models import item,categories
from django.views import View
from .forms import CustomerRegistrationForm,authentication
from django.contrib import messages



def home(request):
 products = item.objects.all()
 return render(request, 'app/home.html',{"products":products,"categories":categories})

def product_detail(request,id):
 prod = item.objects.filter(id=id).first()
 return render(request, 'app/productdetail.html',{'prod':prod})

def add_to_cart(request):
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

# def login(request):
#  return render(request, 'app/login.html')
class login (View):
 def get(request):
  pass

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class customerregistration(View):
 def get (self, request):
  form = CustomerRegistrationForm()
  return render(request, 'app/customerregistration.html', {'form': form})
 def post(self, request):
  form = CustomerRegistrationForm(request.POST)
  print(request.POST['email'])
  if form.is_valid():
   messages.success(request,'User registered successful')
   form.save()
  return render(request, 'app/customerregistration.html', {'form': form})

def checkout(request):
 return render(request, 'app/checkout.html')
