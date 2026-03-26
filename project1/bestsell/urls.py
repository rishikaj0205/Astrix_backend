from django.urls import path
from .views import get_Best,upload_Best

urlpatterns=[
    path('best/',get_Best,name='bestsell'),
    path('upload-best',upload_Best,name="bestupload")
]