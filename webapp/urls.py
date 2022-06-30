from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('login/abc', views.abc, name='abc'),
    path('cart/abc', views.abc, name='abc'),
    path('checkout/', views.checkout, name='checkout'),
    path('remove/', views.remove, name='remove'),
    path('registration/register', views.register, name='register'),
    path('registration/abc', views.abc, name='abc'),
]