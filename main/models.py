from django.db import models
from django.core.cache import cache


class Products(models.Model):
    prod_name = models.CharField(max_length = 100)
    prod_price = models.DecimalField(max_digits=8, decimal_places=2)
    prod_origin = models.CharField(max_length = 100)
    prod_img = models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.prod_name
    
    ################### Overriding save() method of models.Model to delete cache once a new prod added##############
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # this ensures that usual save() method of parent also executed
        cache.delete('home_cache') # this deletes the cache so that home view will load cache again once a prod is added

