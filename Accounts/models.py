from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email= models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    reset_token = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Brands(models.Model):
    brand_name= models.CharField( max_length=100,primary_key=True)
    brand_logo =  models.ImageField( upload_to='images/Brands', height_field=None, width_field=None, max_length=None)
    brand_website = models.URLField(max_length=300)

    def __str__(self):
        return self.brand_name
    
class Product(models.Model):
    URL =  models.URLField(max_length=3000)
    product_name = models.CharField( max_length=255)
    brand_name = models.CharField( max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.DecimalField(default=0,max_digits=4,decimal_places=2)
    image = models.ImageField( upload_to='images/Products', height_field=None, width_field=None, max_length=None)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.brand_name