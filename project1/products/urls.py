# urls.py
from django.urls import path
from .views import get_products, upload_product

urlpatterns = [
    path("products/", get_products),
    path("upload-product/", upload_product),
]