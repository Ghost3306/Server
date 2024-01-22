from django.db import models

class Seller(models.Model):
    bussinessname = models.CharField(max_length=255,null=True,blank=True)
    uniquekey = models.CharField(max_length=255)
    bussinessemail = models.EmailField(default='abc@gmail.com')
    phone = models.CharField(max_length= 10)
    gst = models.CharField(max_length= 50)
    bussimage = models.ImageField(upload_to='')

    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    taluka = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6,default=416602)

    owneremail = models.EmailField(default ='abc@gmail.com')
    ownerphone = models.CharField(max_length=10)
    ownername = models.CharField(max_length=255,null=True,blank=True)

    bankname = models.CharField(max_length=255)
    accno = models.CharField(max_length = 50)
    ifsc = models.CharField(max_length = 25)
    aadharcard = models.CharField(max_length = 20)
    
    password = models.TextField()



