from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from seller.serializers import SellerShowSerializer
from seller.models import Seller
from users.accessibility import gen_api_key
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
import random

@csrf_exempt
def seller(request):
    apikey = gen_api_key()
    seller = Seller.objects.all()
    seller_info = SellerShowSerializer(seller,many=True)
    print(request.method)
    if request.method=='POST':
        while True:
            server_api = Seller.objects.filter(uniquekey=apikey)
            if(len(server_api)==0):
                break
            else:
                apikey=gen_api_key()
        bussinessname = request.POST.get('bussinessname')
        uniquekey = apikey
        bussinessemail = request.POST.get('bussinessemail')
        phone = request.POST.get('phone')
        gst = request.POST.get('gst')
        bussimage =request.FILES['bussimage']

        state =request.POST.get('state')
        district =request.POST.get('district')
        taluka = request.POST.get('taluka')
        city = request.POST.get('city')
        pincode = request.POST.get('pin')

        owneremail = request.POST.get('owneremail')
        ownerphone = request.POST.get('ownerphone')
        ownername = request.POST.get('ownername')

        bankname = request.POST.get('bankname')
        accno = request.POST.get('accno')
        ifsc = request.POST.get('ifsc')
        aadharcard = request.POST.get('aadharcard')
        password = request.POST.get('password')
        print(bussimage)
        seller = Seller(bussinessname=bussinessname,uniquekey=uniquekey,bussinessemail=bussinessemail,phone=phone,gst=gst,bussimage=bussimage,state=state,district=district,taluka=taluka,city=city,pincode=pincode,owneremail=owneremail,ownerphone=ownerphone,ownername=ownername,bankname=bankname,accno=accno,ifsc=ifsc,aadharcard=aadharcard,password=password)
        seller.save()
        context = {
            'bussinessname':bussinessname,
            'uniquekey':uniquekey,
            'bussinessemail':bussinessemail,
            'phone':phone,
            'gst':gst,
            
            'state':state,
            'district':district,
            'taluka':taluka,
            'city':city,
            'owneremail':owneremail,
            'ownerphone':ownerphone,
            'ownername':ownername,
            'bankname':bankname,
            'accno':accno,
            'ifsc':ifsc,
            'aadharcard':aadharcard
           
        }
        return JsonResponse({'status':'200','context':context})
    return JsonResponse(seller_info.data,safe=False)


@csrf_exempt
def login(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')
   
    try:
       
        seller = Seller.objects.all()
        for x in seller:
            try:
                print(x.bussinessemail,x.password)
                if x.bussinessemail==username and x.password==password:
                    print('login success')
                    context = {
                        'uniquekey':x.uniquekey,
                        'name':x.bussinessname,
                        'email':x.bussinessemail
                    }
                    return JsonResponse({'status':'200','message':'User authenticate...Login successful!','data':context})
            except Exception as e:
                print(e)
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
        seller = Seller.objects.all()
        for x in seller:
            print('checking:',x.bussinessemail,x.uniquekey)
            if x.bussinessemail==email and x.uniquekey ==apikey:
                print('found:',x.bussinessemail,x.uniquekey)
                try:
                    seller = Seller.objects.get(bussinessemail=email)
                
                except Exception as e:
                    return JsonResponse({'status':'404','message':'Entered email does not exist'})
                
                try:
                    seller.password = password
                    seller.save()
                    return JsonResponse({'status':'200','message':'Password update successfully'})
                except Exception as e:
                    return JsonResponse({'status':'500','message':'Internal Server Error! failed to update password!...Please try again after some time'})
            
        return JsonResponse({'status':'401','message':'Unauthorized access detected!'})     
    except Exception as e:
        print(e)
        return JsonResponse({'status':'500','message':'Internal Server Error!'})
    

@csrf_exempt
def send_otp(request):
    otp = random.randint(1111,9999)
    to_email = request.POST.get('email')
    apistate = False
    print(to_email)
    api = ''
    try:
        seller = Seller.objects.get(bussinessemail = to_email)
        username = seller.bussinessname
        api = seller.uniquekey
    except:
        # return JsonResponse({'status':'400','message':'Invalid email address....Please reenter email!',})
        username = "Dear Seller"
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
            return JsonResponse({'status':'200','message':'otp send successfully...','otp':otp,'uniquekey':api})
        except BadHeaderError:
            return JsonResponse({'status':'500','message':'Failed to send otp...',})
        
    else:    
        return JsonResponse({'status':'400','message':'Invalid email address....Please reenter email!',})
    
    
    