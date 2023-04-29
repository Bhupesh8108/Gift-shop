from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from .forms import authentication
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home,name='home'),
    path('product-detail/<str:id>', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'app/login.html',authentication_form=authentication), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('registration',views.customerregistration.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
