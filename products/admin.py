from django.contrib import admin
from .models import Category, Product, Photo


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class PhotoInline(admin.TabularInline):
    model = Photo
    max_num = 10
    extra = 3


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'url', 'created']
    list_display_links = []


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
