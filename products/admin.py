from django.contrib import admin
from products.models import Products

class DisplayProducts(admin.ModelAdmin):
    list_display = ('uniqueid' ,'name' ,'price','delivertcharge','sellerid','sellername' ,'state' ,'district', 'selleremail' ,'category', 'image1','image2', 'image3' ,'image4','image5')

admin.site.register(Products,DisplayProducts)
