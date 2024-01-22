from django.http import JsonResponse
from django.shortcuts import render
from seller.models import Seller
from users.accessibility import gen_api_key
from products.models import Products
from products.serializers import ProductsViewSerializer

def addproduct(request):
    sellerid = request.POST.get('sellerid')
    print(sellerid)
    seller = Seller.objects.filter(uniquekey=sellerid)
    seller_name = ''
    seller_state = ''
    seller_district = ''
    sellerr_email = ''
    for x in seller:
        print(x.bussinessname)
        seller_name = x.bussinessname
        seller_state = x.state
        seller_district = x.district
        sellerr_email = x.bussinessemail
        break
    uniqueid = gen_api_key()
    while True:
        server_key = Products.objects.filter(uniqueid=uniqueid)
        if(len(server_key)==0):
            break
        else:
            uniqueid = gen_api_key()
    name = request.POST.get('name')
    price = request.POST.get('price')
    delivertcharge = request.POST.get('delivertcharge')
    
    category = request.POST.get('category')
    image1 = request.POST.get('image1')
    image2 = request.POST.get('image2')
    image3 = request.POST.get('image3')
    image4 = request.POST.get('image4')
    image5 = request.POST.get('image5')
    try:
        seller_obj = Seller(uniqueid= uniqueid,name=name, price=price, delivertcharge=delivertcharge,sellerid=sellerid,sellername=seller_name,state=seller_state,district=seller_district,selleremail=sellerr_email, category=category,image1=image1,image2=image2,image3=image3,image4=image4, image5=image5)
        seller_obj.save()

    except Exception as e:
        print(e)
        
    return JsonResponse({'key':'done'})


def allproduct(request):
    product = Products.objects.all()
    prod_serial = ProductsViewSerializer(product,many=True)
    return JsonResponse(prod_serial.data,safe=False)
