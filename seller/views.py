from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from seller.serializers import SellerShowSerializer
from seller.models import Seller

@csrf_exempt
def seller(request):
    seller = Seller.objects.all()
    seller_info = SellerShowSerializer(seller,many=True)
    print(request.method)
    if request.method=='POST':
        bussinessname = request.POST.get('bussinessname')
        uniquekey = 'unique'
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
        return JsonResponse({'status':200,'context':context})
    return JsonResponse(seller_info.data,safe=False)

