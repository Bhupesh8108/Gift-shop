from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app import views
from .forms import password_set,password_reset_form

urlpatterns = [
    path('', views.home,name='home'),
    path('product-detail/<str:id>', views.product_detail.as_view(), name='product-detail'),
    path('cart/', views.cart, name='cart'),
    path('buy/<str:id>', views.buy_now.as_view(), name='buy-now'),
    path('profile/', views.profile.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('my_orders/', views.my_orders.as_view(), name='my_orders'),
    path('changepassword/', views.change_password , name='changepassword'),
    path('category/<category>', views.category, name='category'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('minuscart/',views.minuscart,name='minuscart'),
    path('pluscart/',views.pluscart,name='pluscart'),
    path('removecart/',views.removecart,name='removecart'),
    path('searchresult/', views.searchresult.as_view(), name='searchresult'),
    path('resetpassword/',views.reset_password.as_view(),name='password_reset'),
    path('password-set/<token>',views.password_set_view.as_view(),name='password_set'),
    path('verifypayment',views.verifypayment.as_view(),name='verifypayment'),
    path('verifycartpayment',views.verifycartpayment.as_view(),name='verifycartpayment'),
    path('top-product',views.top_product.as_view(),name='top-product'),
    path('update_status',views.update_status.as_view(),name='update_status'),
    path('update_product_status/',views.update_product_status.as_view(),name='update_product_status'),
    path('my_product_filter',views.my_product_filter.as_view(),name='my_product_filter'),
    path('stats/',views.stats.as_view(),name='stats'),
    path('add_product',views.add_product.as_view(),name='add_product'),

    # path('resetpassword/',views.reset_password.as_view(),name='password_reset'),
    # path('resetpassword/done/',auth_views.PasswordResetDoneView.as_view(
    # template_name = 'app/reset_done.html'), name='password_reset_done'),
    # path('resetpassword/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
    # template_name = 'app/reset_confirm.html',
    # form_class =password_set), name='password_reset_confirm'),
    # path('resetpassword/complete/',auth_views.PasswordResetCompleteView.as_view(
    # template_name = 'app/reset_complete.html'), name='password_reset_complete'),
    path('registration',views.customerregistration.as_view(), name='customerregistration'),
    path('my_product',views.my_product.as_view(), name='my_product'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
