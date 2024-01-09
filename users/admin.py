from django.contrib import admin
from users.models import Customers

class DisplayUsers(admin.ModelAdmin):
    list_display = ('name','email','phone','address','birthdate','apikey','password')

admin.site.register(Customers,DisplayUsers)
