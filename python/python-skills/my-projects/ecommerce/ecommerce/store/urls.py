from django.urls import path
from . import views

urlpatterns=[
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('updateitem/',views.updateitem,name='updateitem'),
    path('processorder/',views.processorder,name='processorder'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('register/',views.register,name='register'),
]