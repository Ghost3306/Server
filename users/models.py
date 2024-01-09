from django.db import models

class Customers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default = 'default@gmail.com')
    phone = models.IntegerField()
    address = models.TextField()
    birthdate = models.DateField()
    apikey = models.CharField(max_length=64)
    password = models.TextField()


    
