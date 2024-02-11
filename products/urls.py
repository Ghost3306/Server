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
    path('orderplaced/',views.order_placed,name='orderplaced'),
    path('yourordes/',views.yourorders,name='yourorders'),
    path('sellerorders/',views.sellerorders,name='sellerorders'),
    path('cancelorder/',views.cancelorder,name='canelorder'),
    path('placeorder/',views.placeorder,name='placeorder'),
    path('sellerordersNone/',views.sellerordersNone,name='sellerordersNone'),
    path('sellerhistory/',views.sellerhistory,name='sellerhistory'),
    path('sellerallproduct/',views.sellerallproduct,name='sellerallproduct'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)