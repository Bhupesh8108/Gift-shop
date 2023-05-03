from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from .forms import authentication,password_change
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home,name='home'),
    path('product-detail/<str:id>', views.product_detail, name='product-detail'),
    path('cart/', views.cart, name='cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password , name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('minuscart/',views.minuscart,name='minuscart'),
    path('pluscart/',views.pluscart,name='pluscart'),
    path('removecart/',views.removecart,name='removecart'),
    path('searchresult/', views.searchresult, name='searchresult'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('registration',views.customerregistration.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
