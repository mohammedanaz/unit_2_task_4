from django.db import models
from django.contrib.auth.hashers import make_password

class Products(models.Model):
    prod_name = models.CharField(max_length = 100)
    prod_price = models.DecimalField(max_digits=8, decimal_places=2)
    prod_origin = models.CharField(max_length = 100)
    prod_img = models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.prod_name
    

class UserRegister(models.Model):
    f_name = models.CharField(max_length = 100)
    l_name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 250)
    email_id = models.EmailField(max_length = 250)
    password = models.CharField(max_length = 100)

    def save(self, *args, **kwargs):    
        hashed_password = make_password(self.password)
        print('Hashed Password:', hashed_password)
        self.password = hashed_password
        super(UserRegister, self).save(*args, **kwargs)

    def __str__(self):
        return self.username