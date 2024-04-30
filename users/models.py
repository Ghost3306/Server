from django.db import models
from django.utils import timezone


class Customers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default = 'default@gmail.com')
    phone = models.CharField(max_length=10)
    address = models.TextField()
    birthdate = models.DateField()
    apikey = models.CharField(max_length=64)
    password = models.TextField()


class Cart(models.Model):
    productname = models.CharField(max_length=255)
    productid = models.IntegerField()#from client
    price = models.IntegerField()
    delivertcharge = models.IntegerField()
    useruid = models.CharField(max_length=255)#from client
    username = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    quantity = models.CharField(max_length=255)#from client
    sellerid = models.CharField(max_length=255)
    sellername = models.CharField(max_length=255)
    image = models.ImageField(upload_to='',default='default.png')

class SaveLater(models.Model):
    productname = models.CharField(max_length=255)
    productid = models.IntegerField()#from client
    price = models.IntegerField()
    delivertcharge = models.IntegerField()
    useruid = models.CharField(max_length=255)#from client
    username = models.CharField(max_length=255)
    date = models.DateTimeField()
    quantity = models.CharField(max_length=255)#from client
    sellerid = models.CharField(max_length=255)
    sellername = models.CharField(max_length=255)
    image = models.ImageField(upload_to='',default='default.png')

    

    
