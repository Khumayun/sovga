from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "index.html", {})

def contacts_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})

def product_view(request, *args, **kwargs):
	return render(request, "product.html", {})

def product_detail_view(request, *args, **kwargs):
	return render(request, "product-detail.html", {})

def shopping_cart_view(request, *args, **kwargs):
	return render(request, "shopping-cart.html", {})
