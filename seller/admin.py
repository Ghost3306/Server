from django.contrib import admin
from seller.models import Seller

class DisplaySeller(admin.ModelAdmin):
    list_display = ('id','bussinessname' ,'uniquekey', 'bussinessemail' ,'phone' ,'gst','state','district' ,'taluka', 'city', 'owneremail', 'ownerphone', 'ownername' ,'bankname', 'accno' ,'ifsc','aadharcard' )

admin.site.register(Seller,DisplaySeller)
