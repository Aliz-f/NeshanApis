from django.db import models
from django.db.models.base import Model
from location.models import Address

# Create your models here.
class DistanceLocation(models.Model):
    source_address = models.ForeignKey(Address, related_name="source_address", null=True,  on_delete=models.CASCADE)
    destination_address = models.ForeignKey(Address, related_name="destination_address", null=True, on_delete=models.CASCADE)
    distance_km = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
