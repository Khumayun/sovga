from django.views.generic import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def product_list_view(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    paginator = Paginator(products,8) # Show 16 products per page

    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    
    context = {
        'categories': categories,
        'products': paged_products
    }
    return render(request, 'product.html', context)


def product_detail_view(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {
        'product': product
    }
    return render(request, 'product-detail.html', context)


def newfunc(request):
    return request