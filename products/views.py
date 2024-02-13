from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from seller.models import Seller
from users.accessibility import gen_api_key
from products.models import Products
from products.serializers import ProductsViewSerializer,PlaceOrderSerializer
from django.views.decorators.csrf import csrf_exempt
from users.models import Cart
from products.models import PlacedOrder
import random
from datetime import date
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
    page = request.POST.get('page', 1)
    product = Products.objects.filter(sellerid=sellerid)
    
    product_per_page = 10
    paginator = Paginator(product,product_per_page)
    try:
        products = paginator.page(page)
        print(type(products))
    except PageNotAnInteger:
        products = paginator.page(1)

    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    except Exception as e:
        print(e)
    prod_serial = ProductsViewSerializer(products,many=True)
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

@csrf_exempt  
def searchcategory(request):
    inputtext = request.POST.get('input')
    products = Products.objects.filter(category__icontains=inputtext)
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


    
@csrf_exempt
def order_placed(request):
    

    uuid = request.POST.get('uuid')
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    state = request.POST.get('state')
    district = request.POST.get('district')
    taluka = request.POST.get('taluka')
    city = request.POST.get('city')
    landmark = request.POST.get('landmark')
    pincode = request.POST.get('pincode')
    print(uuid)
    cart = Cart.objects.filter(useruid=uuid)
    totalprice = request.POST.get('totalprice')
    dat = date.today()
    payment = request.POST.get('payment')
    for x in cart:
        try:
            sellerid = x.sellerid
            sellername = x.sellername
            try:
                print(x.productid)
                product = Products.objects.filter(uniqueid=x.productid)
                print(len(product))
            except Exception as e:
                print(e)
            for u in product:
                image = u.image1
                break
            orderid = gen_api_key() #uid
            placed = PlacedOrder.objects.filter(uid=orderid)
            while True:
                if len(placed)>=1:
                    orderid = gen_api_key
                else:
                    break
            print(orderid)
            placed_order_obj = PlacedOrder(uid=orderid,uuid=uuid,name=name,email=email,phone=str(phone),state=state,district=district,taluka=taluka,city=city,landmark=landmark,pincode=pincode,sellerid=sellerid,sellername=sellername,product=x.productname,productid=x.productid,delivery=x.delivertcharge,quantity=x.quantity,date=dat,price=x.price,payment=payment,totalprice=totalprice,productimage=image)
            
            placed_order_obj.save()
        except Exception as e:
            print(e)
        

       

    print(sellerid,'seller')
    try:
        
        cart = Cart.objects.filter(useruid=uuid)
        cart.delete()
        return JsonResponse({'status':'200','msg':'order successfully placed...'})
    except Exception as e:
        print(e)
        return JsonResponse({'key':'403'})

@csrf_exempt
def buy_order_placed(request):
    uuid = request.POST.get('uuid')
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    state = request.POST.get('state')
    district = request.POST.get('district')
    taluka = request.POST.get('taluka')
    city = request.POST.get('city')
    landmark = request.POST.get('landmark')
    pincode = request.POST.get('pincode')
    quantity = request.POST.get('quantity')
    productid = request.POST.get('productid')
    payment = request.POST.get('payment')
    dat = request.POST.get('date')
    print(dat)
    product = Products.objects.get(uniqueid=productid)
    print(uuid)
    orderid = gen_api_key()
    placed = PlacedOrder.objects.filter(uid=orderid)
    while True:
        if len(placed)>=1:
            orderid = gen_api_key
        else:
            break
    total_price = (int(product.price)*int(quantity))+int(product.delivertcharge)
    placed_order_obj = PlacedOrder(uid=orderid,uuid=uuid,name=name,email=email,phone=str(phone),state=state,district=district,taluka=taluka,city=city,landmark=landmark,pincode=pincode,sellerid=product.sellerid,sellername=product.sellername,date=dat,product=product.name,productid=productid,delivery=product.delivertcharge,quantity=quantity,price=product.price,payment=payment,totalprice=total_price,productimage=product.image1)
            
    placed_order_obj.save()
    return JsonResponse({'status':'200','msg':'order successfully placed...'})
   
        

     





@csrf_exempt  
def yourorders(request):
    uuid = request.POST.get('uuid')
    placedorders = PlacedOrder.objects.filter(uuid=uuid ).order_by('-id')
    place_serializer = PlaceOrderSerializer(placedorders,many=True)
    return JsonResponse({'response':place_serializer.data})

@csrf_exempt
def sellerorders(request):
    seller = request.POST.get('seller')
    print(seller)
    placedorders = PlacedOrder.objects.filter(sellerid=seller)
    print(len(placedorders))
    place_serializer = PlaceOrderSerializer(placedorders,many=True)
    return JsonResponse({'response':place_serializer.data})
@csrf_exempt
def sellerordersNone(request):
    seller = request.POST.get('seller')
    print(seller)
    placedorders = PlacedOrder.objects.filter(sellerid=seller,delstatus__in=['None','accept','dispatching'])
    print(len(placedorders))
    place_serializer = PlaceOrderSerializer(placedorders,many=True)
    return JsonResponse({'response':place_serializer.data})

@csrf_exempt
def cancelorder(request):
    uid = request.POST.get('uid')
    print(uid)
    try:
        placedorders = PlacedOrder.objects.get(uid=uid)
        placedorders.delstatus='cancelled'
        placedorders.save()
        return JsonResponse({'status':'200'})
    except Exception as e:
        print(e)
        return JsonResponse({'status':'500'})
    
@csrf_exempt
def placeorder(request):
    uid= request.POST.get('uid')
    placeorder= PlacedOrder.objects.filter(uid=uid)
    place = PlaceOrderSerializer(placeorder,many=True)
    return JsonResponse(place.data,safe=False)

@csrf_exempt
def sellerhistory(request):
    seller = request.POST.get('seller')
    print(seller)
    placedorders = PlacedOrder.objects.filter(sellerid=seller,delstatus='delivered')
    print(len(placedorders))
    place_serializer = PlaceOrderSerializer(placedorders,many=True)
    return JsonResponse({'response':place_serializer.data})

@csrf_exempt
def sellerallproduct(request):
    seller = request.POST.get('seller')
    print(seller)
    placedorders = PlacedOrder.objects.filter(sellerid=seller)
    print(len(placedorders))
    place_serializer = PlaceOrderSerializer(placedorders,many=True)
    return JsonResponse({'response':place_serializer.data})

@csrf_exempt
def changestate(request):
    try:
        state = request.POST.get('state')
        uid = request.POST.get('uid')
        courier = request.POST.get('courier')
        datenow = date.today()
        # print(sellerapi)
        if courier==None:
            placeorder = PlacedOrder.objects.get(uid=uid)
            placeorder.delstatus=state
            placeorder.approxdelivery=datenow
            placeorder.save()
        else:
            placeorder = PlacedOrder.objects.get(uid=uid)
            placeorder.delstatus=state
            placeorder.couriername=courier
            placeorder.approxdelivery=datenow
            placeorder.save()
        return JsonResponse({'status':'200'})
    except Exception as e:
        print(e)
        return JsonResponse({'status':'500'})
