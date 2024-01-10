from django.http import JsonResponse
from django.shortcuts import render
from users.models import Customers
from users.accessibility import gen_api_key
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
import random

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


def send_otp(request):
    otp = random.randint(0000,9999)
    to_email = request.GET.get('email')
    username = request.GET.get('name')
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
            return JsonResponse({'status':'200','message':'otp send successfully...','otp':otp})
        except BadHeaderError:
            return JsonResponse({'status':'400','message':'Failed to send otp...',})
        
    else:    
        return JsonResponse({'status':'400','message':'Invalid email address....Please reenter email!',})
