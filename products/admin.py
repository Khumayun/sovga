from django.contrib import admin

from .models import Category, Product

from django.shortcuts import get_object_or_404
from products.models import Product_gallery, Product_image
from multiupload.admin import MultiUploadAdmin

class ImageInlineAdmin(admin.TabularInline):
    model = Product_image

class GalleryMultiuploadMixing(object):

    def process_uploaded_file(self, uploaded, gallery, request):
        if gallery:
            image = gallery.images.create(file=uploaded)
        else:
            image = Image.objects.create(file=uploaded, gallery=None)
        return {
            'url': image.file.url,
            'thumbnail_url': image.file.url,
            'id': image.id,
            'name': image.filename
        }

class GalleryAdmin(GalleryMultiuploadMixing, MultiUploadAdmin):
    inlines = [ImageInlineAdmin,]
    multiupload_form = True
    multiupload_list = False

    def delete_file(self, pk, request):
        '''
        Delete an image.
        '''
        obj = get_object_or_404(Image, pk=pk)
        return obj.delete()


class ImageAdmin(GalleryMultiuploadMixing, MultiUploadAdmin):
    multiupload_form = False
    multiupload_list = True
    multiupload_limitconcurrentuploads = 6


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin, GalleryMultiuploadMixing):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Product_gallery, GalleryAdmin)
admin.site.register(Product_image, ImageAdmin)