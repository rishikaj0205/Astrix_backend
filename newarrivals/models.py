from django.db import models

class newArrivals(models.Model):
    name = models.CharField( )
    price = models.CharField( )
    image = models.ImageField(upload_to="arrivals/")

    def __str__(self):
        return self.name