from django.contrib import admin
from products.models import Products,Review

class DisplayProducts(admin.ModelAdmin):
    list_display = ('uniqueid' ,'name','description' ,'price','delivertcharge','width','height','length','sellerid','sellername' ,'state' ,'district', 'selleremail' ,'category', 'image1','image2', 'image3' ,'image4','image5','rating','len_review')

class DisplayReview(admin.ModelAdmin):
    list_display= ('uid','productname','productid','reviewerid','reviwername','review','star','title')
    
admin.site.register(Products,DisplayProducts)
admin.site.register(Review,DisplayReview)
