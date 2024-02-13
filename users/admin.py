from django.contrib import admin
from users.models import Customers
from users.models import Cart,SaveLater

class DisplayUsers(admin.ModelAdmin):
    list_display = ('id','name','email','phone','address','birthdate','apikey','password')

class CartDisplay(admin.ModelAdmin):
    list_display = ('productname','productid','useruid','username','date','quantity','sellerid','sellername')

class SaveDisplay(admin.ModelAdmin):
    list_display = ('productname','productid','useruid','username','date','quantity','sellerid','sellername')
admin.site.register(Customers,DisplayUsers)
admin.site.register(Cart,CartDisplay)
admin.site.register(SaveLater,SaveDisplay)