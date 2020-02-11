from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('add-category', views.CategoryCreateView.as_view(), name="category_create_view"),
    path('list-categories', views.CategoryListView.as_view(), name="category_list_view"),
    path('update-category', views.CategoryUpdateView.as_view(), name="category_update_view"),
    path('delete-category', views.CategoryDeleteView.as_view(), name="category_delete_view"),

    path('add-product', views.ProductCreateView.as_view(), name="product_create_view"),
    path('list-products', views.ProductListView.as_view(), name="product_list_view"),
    path('update-product', views.ProductUpdateView.as_view(), name="product_update_view"),
    path('delete-category', views.ProductDeleteView.as_view(), name="product_delete_view"),

    path('add-photo', views.PhotoCreateView.as_view(), name="photo_create_view"),
    path('list-photos', views.PhotoListView.as_view(), name="photo_list_view"),
    path('update-photo', views.PhotoUpdateView.as_view(), name="photo_update_view"),
    path('delete-photo', views.PhotoDeleteView.as_view(), name="photo_delete_view"),
]
