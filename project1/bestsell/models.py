from django.db import models

class Bestsellings(models.Model):
    name=models.CharField()
    price=models.CharField()
    image=models.ImageField(upload_to="best/")


    def __str__(self):
        return self.name

