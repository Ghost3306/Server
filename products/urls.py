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
    path('sellerproducts/',views.sellersproducts,name='sellerproducts'),
    path('updateproduct/',views.updateproduct,name='updateproduct'),
    path('searchproduct/',views.searchproduct,name='search'),
    path('searchcategory/',views.searchcategory,name='searchcategory'),
    path('orderplaced',views.order_placed,name='orderplaced')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)