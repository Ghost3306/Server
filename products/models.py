from django.db import models
from django.utils import timezone
class Products(models.Model):
    uniqueid = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(default='none')
    price = models.IntegerField()
    delivertcharge = models.IntegerField()
    width = models.FloatField(null=True,blank=True)
    height = models.FloatField(null=True,blank=True)
    length = models.FloatField(null=True,blank=True)
    sellerid = models.CharField(max_length=255)
    sellername = models.CharField(max_length=255)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    selleremail = models.EmailField(default='abc@gmail.com')
    category = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='',default='default.png')
    image2 = models.ImageField(upload_to='',default='default.png')
    image3 = models.ImageField(upload_to='',default='default.png')
    image4 = models.ImageField(upload_to='',default='default.png')
    image5 = models.ImageField(upload_to='',default='default.png')
    rating = models.IntegerField(default=0)
    len_review =models.IntegerField(default=0)

class Review(models.Model):
    uid = models.IntegerField()
    productname = models.CharField(max_length=255)
    productid = models.IntegerField()
    reviewerid = models.CharField(max_length=255)
    reviwername = models.CharField(max_length=255)
    review = models.TextField()
    star = models.IntegerField()
    title = models.CharField(max_length=255)


class PlacedOrder(models.Model):
    uid = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255,default='0000')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    taluka = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    landmark = models.CharField(max_length=255)
    pincode = models.IntegerField()
    sellerid = models.CharField(max_length=255)
    sellername = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    approxdelivery = models.DateField(blank=True, null=True)
    product = models.CharField(max_length=255)
    productid = models.CharField(max_length=255)
    price = models.IntegerField()
    delivery = models.IntegerField(default=0)
    quantity = models.IntegerField()
    payment = models.CharField(max_length=50)
    totalprice = models.IntegerField()
    couriername = models.CharField(max_length=255,default= 'courier' )
    delstatus = models.CharField(max_length=100)