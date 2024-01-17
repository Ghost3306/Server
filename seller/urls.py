from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from seller import views
# from users import views
urlpatterns = [
    path('showseller/',views.seller,name='showseller')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
