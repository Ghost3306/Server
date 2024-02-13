from django.http import JsonResponse
from django.shortcuts import render
from users.models import Customers
from users.accessibility import gen_api_key
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
import random
from users.models import Cart
from django.views.decorators.csrf import csrf_exempt
from products.models import Products
from seller.models import Seller
from users.models import Cart,SaveLater
from users.serializers import CartShowSerializer,SaveShowSerializer

@csrf_exempt
def customers(request):
    apikey = gen_api_key()
    email = request.POST.get('email')
    #checking for existing api key
    while True:
        server_api = Customers.objects.filter(apikey=apikey)
        if(len(server_api)==0):
            break
        else:
            apikey=gen_api_key()
    #checking for conflit user email and return message
    server_api = Customers.objects.filter(email=email)
    if(len(server_api)!=0):
        return JsonResponse({'status':'409','message':'User already exist..Please Login!'})
    print(len(apikey))
    print("api" ,apikey)
    name = request.POST.get('name')
    
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    birthdate = request.POST.get('birthdate')
    
    password = request.POST.get('password')
    print(name,email,phone,len(phone),address,birthdate,apikey,password)
    try:
        customer_obj = Customers(name=name,email=email,phone=str(phone),address=address,birthdate=birthdate,apikey=apikey,password=password)
        customer_obj.save()
    except Exception as e:
        print(e)
        return JsonResponse({'status':'500','message':'Failed to register user...Please try again!'})

    return JsonResponse({'status':'200','message':'Users account created successful!'})

@csrf_exempt
def send_otp(request):
    otp = random.randint(1111,9999)
    to_email = request.POST.get('email')
    apistate = False
    print(to_email)
    api = ''
    try:
        customers = Customers.objects.get(email = to_email)
        username = customers.name
        api = customers.apikey
    except:
        # return JsonResponse({'status':'400','message':'Invalid email address....Please reenter email!',})
        username = "Dear Customer"
        api = '404'
   
    
    subject = 'One-Time Password (OTP) for Authentication'
    message = f"""
    Dear {username},

    We hope this message finds you well. As part of our commitment to ensuring the security of your account, we have initiated a process that requires your authentication.

    To proceed, please use the following One-Time Password (OTP) within the next 10 minutes on our website:

    OTP: {otp}

    If you did not initiate this authentication process or have any concerns regarding the security of your account, please contact our support team immediately at supportecommerce@gmail.com.

    Thank you for your cooperation in maintaining the security of your account.

    Best regards,
    ECommerce Inc.
    """
    
    from_email = settings.EMAIL_HOST_USER
    
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, [to_email,])
            print('mail send successfully')
            return JsonResponse({'status':'200','message':'otp send successfully...','otp':otp,'apikey':api})
        except BadHeaderError:
            return JsonResponse({'status':'500','message':'Failed to send otp...',})
        
    else:    
        return JsonResponse({'status':'400','message':'Invalid email address....Please reenter email!',})
    

@csrf_exempt
def login(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')
   
    try:
       
        customers = Customers.objects.all()
        for x in customers:
            try:
                print(x.email,x.password)
                if x.email==username and x.password==password:
                    data = {
                        'name':x.name,
                        'email':x.email,
                        'phone':x.phone,
                        'address':x.address,
                        'birthdate':x.birthdate,
                        'apikey':x.apikey,
                        'password':x.password,
                    }
                    return JsonResponse({'status':'200','message':'User authenticate...Login successful!','data':data})
            except Exception as e:
                
                return JsonResponse({'status':'500','message':'Internal Server Error'})
            
        return JsonResponse({'status':'401','message':'User unauthorized...Login failed!'})
    except Exception as e:
        print(str(e))
        return JsonResponse({'status':'500','message':'Internal Server Error'})
    
@csrf_exempt
def forgot_pass(request):
   
    apikey = request.POST.get('apikey')
    email = request.POST.get('email')
    password = request.POST.get('password')
    print('email',email,password,apikey)
    try:
        customers = Customers.objects.all()
        for x in customers:
            print('checking:',x.email,x.apikey)
            if x.email==email and x.apikey ==apikey:
                print('found:',x.email,x.apikey)
                try:
                    customers = Customers.objects.get(email=email)
                
                except Exception as e:
                    return JsonResponse({'status':'404','message':'Entered email does not exist'})
                
                try:
                    customers.password = password
                    customers.save()
                    return JsonResponse({'status':'200','message':'Password update successfully'})
                except Exception as e:
                    return JsonResponse({'status':'500','message':'Internal Server Error! failed to update password!...Please try again after some time'})
            
        return JsonResponse({'status':'401','message':'Unauthorized access detected!'})     
    except:
        return JsonResponse({'status':'500','message':'Internal Server Error!'})

@csrf_exempt   
def addcart(request):
    productuid = request.POST.get('productid')
    useruid = request.POST.get('apikey')
    qunti = request.POST.get('quntity')
    product = Products.objects.filter(uniqueid=productuid)
    user = Customers.objects.filter(apikey=useruid)
    productname=''
    price=''
    username=''
    sellerid=''
    sellername=''
    for x in product:
        productname=x.name
        price =x.price
        sellerid = x.sellerid
        sellername = x.sellername
        image = x.image1
        delivery = x.delivertcharge
        break
    for x in user:
        username = x.name
    try:
        # print(type(useruid),type(qunti))
        cart_obj = Cart(productname=productname,productid=productuid,price=price,useruid=useruid,username=username,quantity=qunti,sellerid=sellerid,sellername=sellername,image=image,delivertcharge=delivery)
        cart_obj.save()
        return JsonResponse({'status':'200','message':'cart added successfully'})
    except Exception as e:
        print(e)
        return JsonResponse({'status':'500','message':'Internal Server Error!'})
    
@csrf_exempt
def showcart(request):
    uuid = request.POST.get('useruid')
    cart = Cart.objects.filter(useruid=uuid)
    total  = 0
    deli = 0
    for x in cart:
        total+=(x.price*int(x.quantity))
        deli +=x.delivertcharge
    
    cart_serializer = CartShowSerializer(cart,many=True)
    context = {
        'order_total':total,
        'delivery':deli,
        'data':cart_serializer.data,
        'len':len(cart),
        'total':total+deli

    }
    return JsonResponse(context)
@csrf_exempt
def delcart(request):
    try:    
        uniqueid = request.POST.get('cartid')
        print('uniqueid',uniqueid)
        cart = Cart.objects.filter(id=uniqueid)
        for x in cart:
            print(x.productname)
        cart.delete()

        return JsonResponse({'status':'200'})
    except Exception as e:
        print(e)
        return JsonResponse({'status':'403'})
    
@csrf_exempt
def addsavelater(request):
    id = request.POST.get('id')
    try:
        cart_item = Cart.objects.get(id=id)
        print(cart_item.productid)
        savelater_obj = SaveLater(productname=cart_item.productname,productid=cart_item.productid,price=cart_item.price,useruid=cart_item.useruid,username=cart_item.username,quantity=cart_item.quantity,sellerid=cart_item.sellerid,sellername=cart_item.sellername,image=cart_item.image,delivertcharge=cart_item.delivertcharge)
        savelater_obj.save()
        cart_item = Cart.objects.get(id=id)
        cart_item.delete()
        return JsonResponse({'status':'200'})
    except Exception as e:
        print(e)
        return JsonResponse({'status':'403'})

@csrf_exempt
def showsavelater(request):
    uuid = request.POST.get('uuid')
    save = SaveLater.objects.filter(useruid=uuid)
    saveserializer = SaveShowSerializer(save,many=True)
    return JsonResponse(saveserializer.data,safe=False)

@csrf_exempt 
def delsavelater(request):
    try:    
        id = request.POST.get('id')
        print('uniqueid',id)
        cart = SaveLater.objects.filter(id=id)
        for x in cart:
            print(x.productname)
        cart.delete()

        return JsonResponse({'status':'200'})
    except Exception as e:
        print(e)
        return JsonResponse({'status':'403'})



    

    

    
    
    
    
    