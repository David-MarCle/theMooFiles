from django.db import models

class Abductions(models.Model):
        
        latitude = models.DecimalField(max_digits=128, decimal_places=124)
        longitude = models.DecimalField(max_digits=128, decimal_places=124)
        name = models.CharField(max_length=64)
        place = models.CharField(max_length=64)
        description = models.TextField()
        photo=models.CharField(max_length=128)

        def __str__(self):
            return self.name
        
        

