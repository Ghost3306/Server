from django.contrib import admin
from seller.models import Seller,SellerBanner

class DisplaySeller(admin.ModelAdmin):
    list_display = ('id','bussinessname' ,'uniquekey', 'bussinessemail' ,'phone' ,'gst','state','district' ,'taluka', 'city', 'owneremail', 'ownerphone', 'ownername' ,'bankname', 'accno' ,'ifsc','aadharcard' )

class DisplaySellerBanner(admin.ModelAdmin):
    list_display = ('sellerid','banner')

admin.site.register(Seller,DisplaySeller)
admin.site.register(SellerBanner,DisplaySellerBanner)
