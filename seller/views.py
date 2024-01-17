from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from seller.serializers import SellerShowSerializer
from seller.models import Seller

@csrf_exempt
def seller(request):
    seller = Seller.objects.all()
    seller_info = SellerShowSerializer(seller,many=True)
    
    return JsonResponse(seller_info.data,safe=False)