from django.http import HttpResponse
from django.shortcuts import render

from products.models import Product
# Create your views here.
def home_view(request, *args, **kwargs):
	sortby = request.GET.get('sortby', '-created_at')
	products = Product.objects.filter(available=True).order_by(sortby)[:8]
	context={
		'products':products
	}
	return render(request, "index.html", context)

def contacts_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})

def shopping_cart_view(request, *args, **kwargs):
	return render(request, "shopping-cart.html", {})
