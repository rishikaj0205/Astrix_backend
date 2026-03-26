from django.urls import path
from .views import get_arrivals, upload_arrivals

urlpatterns = [
    path("arrivals/", get_arrivals),
    path("upload-arrivals/", upload_arrivals),
]