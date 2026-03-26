from django.db import models

class Product(models.Model):
    name = models.CharField( )
    price = models.CharField( )
    image = models.ImageField(upload_to="products/")
    category= models.CharField()

    def __str__(self):
        return self.name