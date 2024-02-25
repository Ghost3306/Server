from django.db import models

# Create your models here.
class PaymentHistory(models.Model):
    sellerid = models.CharField(max_length=64)
    userid = models.CharField(max_length=60)
    payment_id = models.CharField(max_length=100,verbose_name="Payment ID")
    order_id = models.CharField(max_length=100,verbose_name="Order ID")
    signature = models.CharField(max_length=200,verbose_name="Signature")
    amount = models.IntegerField(verbose_name="Amount")
    datetime = models.DateTimeField(auto_now_add=True)
