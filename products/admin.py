from django.contrib import admin
from products.models import Products,Review,PlacedOrder

class DisplayProducts(admin.ModelAdmin):
    list_display = ('uniqueid' ,'name','description' ,'price','delivertcharge','width','height','length','sellerid','sellername' ,'state' ,'district', 'selleremail' ,'category', 'image1','image2', 'image3' ,'image4','image5','rating','len_review')

class DisplayReview(admin.ModelAdmin):
    list_display= ('productname','productid','reviewerid','reviwername','review','star','title')

class DisplayPlacedOrders(admin.ModelAdmin):
    list_display =('uid' ,'name' ,'email' ,'phone','state' ,'district' ,'taluka','city' ,'landmark', 'sellerid' ,'sellername','date' ,'approxdelivery' ,'payment', 'totalprice' ,'couriername' ,'delstatus') 
admin.site.register(Products,DisplayProducts)
admin.site.register(Review,DisplayReview)
admin.site.register(PlacedOrder,DisplayPlacedOrders)
