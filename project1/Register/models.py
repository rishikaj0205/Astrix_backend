from django.db import models

class Regform(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField( unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name