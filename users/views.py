from django.http import JsonResponse
from django.shortcuts import render
from users.models import Customers
from users.accessibility import gen_api_key


def customers(request):
    apikey = gen_api_key()
    email = request.GET.get('email')
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
    name = request.GET.get('name')
    
    phone = request.GET.get('phone')
    address = request.GET.get('address')
    birthdate = request.GET.get('birthdate')
    
    password = request.GET.get('password')
    # print(name,email,phone,address,birthdate,apikey,password)
    customer_obj = Customers(name=name,email=email,phone=phone,address=address,birthdate=birthdate,apikey=apikey,password=password)
    customer_obj.save()
    
    return JsonResponse({'status':'200','message':'Users account created successful!'})
