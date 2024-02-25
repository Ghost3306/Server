from django.urls import path
from razorpaygate import views

urlpatterns = [
   path('create/',views.create_order,name='create-order-api'),
    path('complete/',views.complete_order,name='complete-order-api')
]
