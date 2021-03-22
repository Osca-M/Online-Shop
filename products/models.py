import uuid
from django.db import models
from django.utils.text import slugify

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Category(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    @property
    def product_count(self):
        return self.product_set.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    category = models.ForeignKey(Category, related_name='product_category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    @property
    def image_list(self):
        return [photo.image.url for photo in self.photo_set.all()]


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_photos')
    image = models.ImageField(upload_to='products/%Y/%m%d', verbose_name='Product Image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Image for %s' % self.product.name

    @property
    def property_name(self):
        return self.product.name

    @property
    def url(self):
        return self.image.url


# class Cart(models.Model):
#     date_created = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=255, blank=True, null=True)
#     user = models.ForeignKey(User, related_name="user_carts")
#     items = models.ManyToManyField(Product)
#
#
