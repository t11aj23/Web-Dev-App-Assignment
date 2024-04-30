from django.shortcuts import render, redirect 
from django.contrib.auth.hashers import check_password 
from main.models.customer import Customer 
from django.views import View 
from main.models.products import Products 
from main.models.orders import Order 
from django.contrib.auth import authenticate, login, logout

'''view for orders'''

class OrderView(View): 

	def get(self, request): 
		customer = request.session.get('customer') 
		orders = Order.get_orders_by_customer(customer) 
		print(orders) 
		return render(request, 'orders.html', {'orders': orders}) 
