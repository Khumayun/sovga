"""sovga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view, contacts_view, about_view, product_view, product_detail_view, shopping_cart_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('contacts/', contacts_view),
    path('about/', about_view),
    path('product/', product_view),
    path('product-detail/', product_detail_view),
    path('cart/', shopping_cart_view),
]


from django.conf.urls import url
#from . import views
#
# #app_name = 'shop'
#
# urlpatterns = [
#     url(r'^$', views.product_list, name='product_list'),
#     url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
#     url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
# ]