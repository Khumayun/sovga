from django.views.generic import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Tag, Holiday
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def product_list_view(request, category_slug=None):

    sortby = request.GET.get('sortby', 'name')
    priceRange_low = request.GET.get('price_range_l', '0')
    priceRange_up = request.GET.get('price_range_u', '100000000000000')
    event = request.GET.get('event', '')
    tag = request.GET.get('tag', '')

    category = None
    categories = Category.objects.all()
    tags = Tag.objects.all()
    holidays = Holiday.objects.all()

    if priceRange_low != '':
        products = Product.objects.filter(
            price__gte = priceRange_low
        )
    if priceRange_up != '':
        products = Product.objects.filter(
            price__lte = priceRange_up
        )
    if event != '':
        products = Product.objects.filter(
            holiday__exact = holidays.get(name__exact = event)
        )
    if tag != '':
        products = Product.objects.filter(
            tag__exact = tags.get(name__exact = tag)
        )


    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    if sortby == 'newness':
        products = products.order_by('created_at')
    else:
        products = products.order_by(sortby)

    paginator = Paginator(products,8) # Show 16 products per page

    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    
    context = {
        'categories': categories,
        'products': paged_products,
        'tags': tags,
        'holidays': holidays
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