from django.contrib import admin
from django.urls import path
from users import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('registercustomer/',views.customers,name='registercustomer'),
    path('sendotp/',views.send_otp,name='sendotp')
]