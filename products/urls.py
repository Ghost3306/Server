from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from products import views
# from users import views
urlpatterns = [
    path('addproduct/',views.addproduct,name='addproducts'),
    path('allproduct/',views.allproduct,name='allproduct'),
    path('deleteproduct/',views.deleteproduct,name='deleteproduct'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)