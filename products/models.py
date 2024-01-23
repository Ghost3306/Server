from django.db import models

class Products(models.Model):
    uniqueid = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(default='none')
    price = models.IntegerField()
    delivertcharge = models.IntegerField()
    sellerid = models.CharField(max_length=255)
    sellername = models.CharField(max_length=255)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    selleremail = models.EmailField(default='abc@gmail.com')
    category = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    image3 = models.ImageField(upload_to='')
    image4 = models.ImageField(upload_to='')
    image5 = models.ImageField(upload_to='')