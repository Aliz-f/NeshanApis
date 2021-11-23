from django.db import models

# Create your models here.
class Address(models.Model):
    latitude = models.CharField(max_length=50)
    longtitude = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=2000)


    def __str__(self):
        if self.address:
            return self.address
        elif self.city:
            return self.city
        else:
            return self.state