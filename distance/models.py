from django.db import models
from django.db.models.base import Model
from location.models import Address

# Create your models here.
class Distance(models.Model):
    source_address = models.ForeignKey(Address, related_name="source_address", null=True,  on_delete=models.CASCADE)
    destination_address = models.ForeignKey(Address, related_name="destination_address", null=True, on_delete=models.CASCADE)
    distance_km = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)

    def __str__(self):
        if self.source_address.address and self.destination_address.address:
            string = '{} - {}'.format(self.source_address.address, self.destination_address.address )
            return string
        elif self.source_address.city and self.destination_address.city:
            string = '{} - {}'.format(self.source_address.city, self.destination_address.city )
            return string
        else:
            string = '{} - {}'.format(self.source_address.state, self.destination_address.state )
            return string