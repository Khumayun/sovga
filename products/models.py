from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name        

    def get_absolute_url(self):
        return reverse('prod_category', kwargs={"category_slug": self.slug })

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=100, db_index=True, blank=True)
    slug = models.SlugField(max_length=100, db_index=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

class Product_gallery(models.Model):
    class Meta:
        verbose_name_plural = 'Galleries'
    title = models.CharField('Title', max_length=20)

    def __str__(self):
        return self.title


class Product_image(models.Model):
    file = models.FileField('File', upload_to='photos/%Y/%m/%d/')
    gallery = models.ForeignKey('Product_gallery', related_name='images', blank=True, null=True, on_delete=True)

    def __str__(self):
        return self.filename

    # def get_absolute_url(self):
    #     return reverse('shop:product_detail', args=[self.id, self.slug])
