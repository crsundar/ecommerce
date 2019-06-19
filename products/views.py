from django.shortcuts import render
from .models import Product 


def home(request):
	context = {'title' : 'home'}
	return render(request, 'products/home.html', context)


def all(request):
 	products = Product.objects.all()
 	context = {'products': products}
 	return render(request, 'products/all.html', context)