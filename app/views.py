from django.shortcuts import render, get_object_or_404, redirect
from .models import item, categories, wishlist, order,search,forget_password
from django.views import View
from rest_framework.views import APIView
from .forms import CustomerRegistrationForm, authentication, password_change, customerprofileform, customer,password_reset_form,password_set
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.views import LoginView, PasswordChangeView
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity
from django.db.models import Q
from django.urls import reverse
import uuid,requests
from django.db.models.functions import Random
from .logic import send_reset_link,send_order_mail
import datetime as dt
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.response import Response
from django.utils.decorators import method_decorator
import time


def home(request):
    products = item.objects.all().order_by(Random())
    orders_by_product = order.objects.values('product').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')
    ids = [product['product'] for product in orders_by_product]
    return render(request, 'app/home.html', {"trending":ids ,"products":products,"categories": categories})


class product_detail(View):
    def get(self,request,id):
        prod = item.objects.filter(id=id).first()
        products = item.objects.all().order_by(Random())
        product = item.objects.get(id=id)
        if request.user.is_authenticated and wishlist.objects.filter(product=product, user=request.user).exists():
            btn_text = "Remove from cart"
        else:
            btn_text = "Add to cart"
        return render(request, 'app/productdetail.html', {'prod': prod, "products": products,'btn_text': btn_text})

    def post(self,request,id):
        product = item.objects.get(id=id)
        if wishlist.objects.filter(product=product, user=request.user).exists():
            wishlist.objects.filter(user=request.user, product=product).delete()
            messages.warning(request, 'Product removed from cart')
        else:
            wishlist(user=request.user, product=product, quantity=1).save()
            messages.success(request, 'Product added to cart')
        return redirect(f'/product-detail/{id}')        

def login(request):
    pid = request.GET.get('product_id')
    if pid:
        return LoginView.as_view(template_name='app/login.html', authentication_form=authentication, next_page=f'/product-detail/{pid}')(request)
    else:
        return LoginView.as_view(template_name='app/login.html', authentication_form=authentication, next_page='/')(request)


def update_price(request):
    user = request.user
    cart_items = wishlist.objects.filter(user=user)
    price = 0
    for cart_item in cart_items:
        price += int(cart_item.product.price) * int(cart_item.quantity)
    return price, cart_items


def cart(request):
    try:
        cart_id = request.GET.get('cart_id')
        wishlist.objects.filter(id=cart_id).delete()
    except:
        pass
    price, cart_items = update_price(request)
    return render(request, 'app/addtocart.html', {'cart_items': cart_items, 'price': float(price), 'total': float(price+50)})


def pluscart(request):
    if request.method == 'GET':
        pid = request.GET.get('produc_id')
        if pid:
            items = get_object_or_404(wishlist, product=pid, user=request.user)
            items.quantity += 1
            items.save()
            price, cart_items = update_price(request)
            data = {'quantity': items.quantity,
            'price': price,
            'total': price+50}
            return JsonResponse(data)


def minuscart(request):
    if request.method == 'GET':
        pid = request.GET.get('produc_id')
        if pid:
            items = get_object_or_404(wishlist, product=pid, user=request.user)
            items.quantity -= 1
            items.save()
            if items.quantity <= 0:
                wishlist.objects.filter(
                    product=pid, user=request.user).delete()

    price, cart_items = update_price(request)
    data = {'quantity': items.quantity,
            'price': price,
            'total': price+50,
            }
    return JsonResponse(data)


def removecart(request):
    if request.method == 'GET':
        pid = request.GET.get('produc_id')
        if pid:
            items = get_object_or_404(wishlist, product=pid, user=request.user)
            if items.quantity <= 0:
                wishlist.objects.filter(
                    product=pid, user=request.user).delete()

    price, _ = update_price(request)
    data = {'quantity': items.quantity,
            'price': price,
            'total': price+50}
    return JsonResponse(data)



class profile(View):
    def get(self, request):
        form = customerprofileform()
        return render(request, 'app/profile.html', {'form': form})

    def post(self, request):
        form = customerprofileform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            main_address = form.cleaned_data['main_address']
            street_address = form.cleaned_data['street_address']
            additional_address = form.cleaned_data['additional_address']
            phone_number = form.cleaned_data['phone_number']
            ip, routable = get_client_ip(request)
            country = "unknown"
            if ip:
                country = DbIpCity.get(ip, api_key="free").country
                if customer.objects.filter(name=name,user=request.user).exists():
                    messages.warning(request,f"{name}'s adress alredy exists")
                else:
                    profile = customer(name=name, main_address=main_address, street_address=street_address,
                                      additional_address=additional_address, phone_number=phone_number, country=country)
                    profile.user = request.user
                    profile.save()
                    messages.success(request, "Address added successfully")
        return render(request, 'app/profile.html',{'form':form})




    

def address(request):
    addresses = customer.objects.filter(user=request.user)
    try:
        cart_id = request.GET.get('cart_id')
        customer.objects.filter(id=cart_id).delete()
    except:
        pass
    return render(request, 'app/address.html',{"addresses" : addresses})




def orders(request):
    cart_items = order.objects.filter(user=request.user).order_by('-date')
    return render(request, 'app/orders.html',{"cart_items" : cart_items})



def change_password(request):
    return PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=password_change,success_url='/')(request)
 


def category(request,category):
    print(category)
    products = item.objects.filter(category=category).order_by(Random())
    return render(request, 'app/category.html',dict(products=products,category= category))



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
                        return redirect(reverse('login'))
        return render(request, 'app/customerregistration.html', {'form': form})





class buy_now(View):
    def post(self, request,id):
        product_query = item.objects.filter(id=id).first()
        actual_shipping_address_id= request.POST.get('add')
        shipping_addresses = customer.objects.filter(user=request.user)
        if shipping_addresses and actual_shipping_address_id:
            actual_shipping_address = get_object_or_404(customer,id=actual_shipping_address_id)
            
        return render(request, 'app/buynow.html',dict(product = product_query,quantity=1,total=product_query.price+50,shipping_addresses=shipping_addresses))
        
        


class searchresult(View):
    def get(self, request):
        search_text = request.GET.get('search')
        if request.user.is_authenticated:
            username = request.user
        else:
            username = get_object_or_404(User, username='anonymous')
        ip = get_client_ip(request)[0]
        search(searchtext=search_text,user=username,ip=ip).save()
        search_items = item.objects.filter(Q(name__contains =search_text) | Q(description__contains=search_text))
        # request.session['search_items'] = list(search_items.values())
        request.session['search_text'] = search_text
        return render(request, 'app/searchresult.html',{'search_text': search_text,'search_items':search_items,'x':len(search_items)})
    def post(self, request):
        slider_value = request.POST.get('price_range')
        id_list = []
        search_text = request.session.get('search_text')
        search_items = item.objects.filter(Q(name__contains =search_text) | Q(description__contains=search_text))
        search_items = search_items.filter(price__lte = slider_value)
        return render(request, 'app/searchresult.html',{'search_items':search_items,'price_range':slider_value,'search_text': search_text,'x':len(search_items)})
        

class reset_password(View):
    def post(self,request):
        email = request.POST.get('email')
        user_detail = User.objects.filter(Q(username=email)| Q(email=email))
        if user_detail.exists():
            user_email = user_detail[0].email
            token = uuid.uuid4()
            try :
                forgot_password_user = forget_password.objects.get(user=user_detail[0])
                forgot_password_user.forgot_password_token=token
                forgot_password_user.save()
            except:
                forget_password(user=user_detail[0],forgot_password_token=token).save()
            send_reset_link(token,user_email)
            messages.success(request,f"Password reset link sent to:{user_email}")
            return redirect(reverse('password_reset'))
        else:
            messages.warning(request,"No user found with given email")
            return redirect('password_reset')
        
    def get(self,request):
        form = password_reset_form()
        return render(request, 'app/reset_password.html',{'form':form})
    
class password_set_view(View):
    def get(self,request,token):
        user_name = forget_password.objects.filter(Q(forgot_password_token=token)).first()
        print(user_name)
        user_query = User.objects.filter(Q(username=user_name)).first()
        form = password_set(user=user_query)
        return render(request, 'app/reset_confirm.html',dict(form=form))    
    def post(self, request,token):
        new_password =  request.POST.get('new_password1')
        confirm_password = request.POST.get('new_password2')
        valid_time = dt.datetime.today() - dt.timedelta(minutes=5)
        try:
            user_name = forget_password.objects.filter(Q(forgot_password_token=token,created_at__gte=valid_time))
            user_query = User.objects.get(username=user_name[0])
            if new_password != confirm_password:
                messages.warning(request,'Two password didnot match')
                form = password_set(user=user_query)
                return render(request, 'app/reset_confirm.html',dict(form=form)) 

            elif len(new_password) < 8:
                messages.error(request,'password must be of 8 character')
                form = password_set(user=user_query)
                return render(request, 'app/reset_confirm.html',dict(form=form)) 

            else:
                user_query.set_password(new_password)
                user_query.save()
                messages.success(request,'Password reset successfully')
                user_name.delete()
                return redirect('login')
        except:
            messages.error(request,'This link has been expired, Please try again')
            return render(request, 'app/reset_confirm.html')
         



@method_decorator(csrf_exempt, name='dispatch')
class verifypayment(View):
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        amount = request.GET.get('amount')
        pid = request.GET.get('product_id')
        add = request.GET.get('address')
        print (add)
        print(token, amount, pid)
        payload = {
            "token":token,
            "amount":amount,
        }
        headers = {
            "Authorization": "Key {}".format(settings.KHALTI_SECRET_KEY)
        }

        response = requests.post(settings.KHALTI_VERIFY_URL,payload,headers=headers).json()
        if response.get("idx"):
            success = True
            products = item.objects.filter(id = pid)
            actual_shipping_address = customer.objects.filter(id = add).first()
            address = f'{actual_shipping_address.main_address} {actual_shipping_address.street_address} near {actual_shipping_address.additional_address}'
            for product in products:
                order(product=product,user=request.user,quantity = 1,status="Pending",price=product.price,address=actual_shipping_address).save()
                send_order_mail(request.user.email,product.id,1,address,actual_shipping_address.phone_number,request.user)

        else:
            success=False
        data = {"success": success}
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class verifycartpayment(View):
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        amount = request.GET.get('amount')
        add = request.GET.get('address')
        payload = {
            "token":token,
            "amount":amount,
        }
        headers = {
            "Authorization": "Key {}".format(settings.KHALTI_SECRET_KEY)
        }

        response = requests.post(settings.KHALTI_VERIFY_URL,payload,headers=headers).json()
        if response.get("idx"):
            success = True
            price,cart_items = update_price(request)
            print(price+50,amount)
            actual_shipping_address = customer.objects.filter(id = add).first()
            for item in cart_items:
                quantity= item.quantity
                orders = order(price=item.product.price*item.quantity,product=item.product.id,user=request.user,address=actual_shipping_address,quantity=quantity)
                orders.save()
                address = f'{actual_shipping_address.main_address} {actual_shipping_address.street_address} near {actual_shipping_address.additional_address}'
                send_order_mail(request.user.email,item.product,quantity,address,actual_shipping_address.phone_number,request.user)
            wishlist.objects.filter(user=request.user).delete()

        else:
            success=False
        data = {"success": success}
        return JsonResponse(data)




def checkout(request):
    price,cart_items = update_price(request)
    shipping_addresses = customer.objects.filter(user=request.user)
    price,cart_items = update_price(request)
    return render(request, 'app/checkout.html',{'cart_items': cart_items, 'shipping_addresses': shipping_addresses,'price': price,'total':price+50})





class my_product(View):
    def get(self, request):
        cart_items = item.objects.filter(seller=request.user).order_by('-date')
        return render(request, 'app/my_product.html',{"cart_items" : cart_items})
    