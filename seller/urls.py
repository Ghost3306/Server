from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from seller import views
# from users import views
urlpatterns = [
    path('showseller/',views.seller,name='showseller'),
    path('login/',views.login,name='login'),
    path('forgot/',views.forgot_pass,name='forgot'),
    path('sendotp/',views.send_otp,name='sendotp'),
    path('banner/',views.addbanner,name='banner'),
    path('allbanner/',views.sellerbanner,name='allbanner'),
    path('deletebanner/',views.deletebanner,name='deletebanner')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
