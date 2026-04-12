# urls.py
from django.urls import path
from .views import get_products, upload_product

urlpatterns = [
    path("productsadd/", get_products),
    path("upload-product/", upload_product),
]