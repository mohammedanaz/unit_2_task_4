from django.db import models


class Products(models.Model):
    prod_name = models.CharField(max_length = 100)
    prod_price = models.DecimalField(max_digits=8, decimal_places=2)
    prod_origin = models.CharField(max_length = 100)
    prod_img = models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.prod_name
    

