from django.contrib import admin 
from django.urls import path 
from .views.home import Index, store 
from .views.signup import Signup 
from .views.login import Login, logout 
from .views.cart import Cart 
from .views.checkout import CheckOut 
from .views.orders import OrderView 
from django.contrib.auth import authenticate, login, logout

urlpatterns = [ 
	path('', Index.as_view(), name='homepage'), 
	path('store', store, name='store'), 

	path('signup', Signup.as_view(), name='signup'), 
	path('login', Login.as_view(), name='login'), 
	path('logout', logout, name='logout'), 
	path('check-out', CheckOut.as_view(), name='checkout'), 

] 
