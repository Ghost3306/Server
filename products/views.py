from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from seller.models import Seller
from users.accessibility import gen_api_key
from products.models import Products
from products.serializers import ProductsViewSerializer
from django.views.decorators.csrf import csrf_exempt
import random

@csrf_exempt
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
    uniqueid = random.randint(11111,99999)
    while True:
        server_key = Products.objects.filter(uniqueid=uniqueid)
        if(len(server_key)==0):
            break
        else:
            uniqueid = random.randint(11111,99999)
    name = request.POST.get('name')
    descrription = request.POST.get('describe')
    price = request.POST.get('price')
    delivertcharge = request.POST.get('delivertcharge')
    width = request.POST.get('width')
    height = request.POST.get('height')
    length = request.POST.get('length')
    category = request.POST.get('category')
    image1 = request.FILES['image1']
    image2 =request.FILES['image2']
    image3 = request.FILES['image3']
    image4 = request.FILES['image4']
    image5 = request.FILES['image5']
    print(image1,image2,image3,image4,image5)
    try:
        seller_obj = Products(uniqueid= uniqueid,name=name, price=price, description=descrription,delivertcharge=delivertcharge,width=width,height=height,length=length,sellerid=sellerid,sellername=seller_name,state=seller_state,district=seller_district,selleremail=sellerr_email, category=category,image1=image1,image2=image2,image3=image3,image4=image4, image5=image5)
        seller_obj.save()
        return JsonResponse({'status':'200','message':'product added successful'})
    except Exception as e:
        print(e)
        
    return JsonResponse({'key':'done'})

@csrf_exempt
def allproduct(request):
    page = request.POST.get('page', 1)
    product = Products.objects.all()
    print(request.method)
    print(page)
    product_per_page = 10
    paginator = Paginator(product,product_per_page)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)

    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    prod_serial = ProductsViewSerializer(product,many=True)
    return JsonResponse(products,safe=False)

@csrf_exempt
def sellersproducts(request):
    sellerid = request.POST.get('sellerapi')
    product = Products.objects.filter(sellerid=sellerid)
    prod_serial = ProductsViewSerializer(product,many=True)
    return JsonResponse(prod_serial.data,safe=False)


@csrf_exempt
def deleteproduct(request):
    try:    
        uniqueid = request.POST.get('uniqueid')
        print(uniqueid)
        products = Products.objects.filter(uniqueid=uniqueid)
        for x in products:
            print(x.name)
        products.delete()

        return JsonResponse({'status':'200'})
    except:
        return JsonResponse({'status':'403'})
    
@csrf_exempt
def updateproduct(request):
    try:
        uniqueid = request.POST.get('uniqueid')
        name = request.POST.get('name')
        descrription = request.POST.get('describe')
        price = request.POST.get('price')
        delivertcharge = request.POST.get('delivertcharge')
        width = request.POST.get('width')
        height = request.POST.get('height')
        length = request.POST.get('length')
        category = request.POST.get('category')
        image1 = request.FILES['image1']
        image2 =request.FILES['image2']
        image3 = request.FILES['image3']
        image4 = request.FILES['image4']
        image5 = request.FILES['image5']

        print(uniqueid,name)
        products = Products.objects.get(uniqueid=uniqueid)
        products.name = name
        products.description = descrription
        products.price = price
        products.delivertcharge = delivertcharge
        products.width = width
        products.height=height
        products.length = length
        products.category =category
        products.image1 = image1
        products.image2 = image2
        products.image3 = image3
        products.image4 = image4
        products.image5 = image5
        products.save()
        return JsonResponse({'status':'200'})
    except:
        return JsonResponse({'status':'403'})

@csrf_exempt  
def searchproduct(request):
    inputtext = request.POST.get('input')
    products = Products.objects.filter(name__icontains=inputtext)
    page = request.POST.get('page', 1)

    product_per_page = 10
    paginator = Paginator(products,product_per_page)
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)

    except EmptyPage:
        product = paginator.page(paginator.num_pages)
  
    prodserializer = ProductsViewSerializer(product,many=True)
    return JsonResponse(prodserializer.data,safe=False)


    

   
