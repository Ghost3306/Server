from django.shortcuts import render
from django.http import JsonResponse
from razorpaygate.razorpay.main import RazorpayClient
from razorpaygate.models import PaymentHistory
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
rz = RazorpayClient()

@csrf_exempt
def create_order(request):
    if request.method=='POST':
        amount = int(request.POST.get('amount'))
        currency=request.POST.get('currency')
        print('cred',settings.RAZORPAY_KEY_ID,settings.RAZORPAY_SECRET_ID)
        
        try:
            order_response = rz.create_order(amount=amount,currency=currency)
            return JsonResponse({'orderdata':order_response})
        except Exception as e:
            print(e)
            return JsonResponse({'orderdata':'order failed','status':'400'})
        
@csrf_exempt
def complete_order(request):
    if request.method=='POST':
        order_id = request.POST.get('order_id')
        payment_id =request.POST.get('payment_id')
        signature=request.POST.get('signature')
        amount=int(request.POST.get('amount'))
        userid = request.POST.get('userid')
        sellerid =request.POST.get('sellerid')
        print(order_id,payment_id,signature)
        try:
            rz.verify_payment(
                razorpay_order_id=order_id,
                razorpay_payment_id=payment_id,
                razorpay_signature=signature
            )
            payment_history_obj = PaymentHistory(userid=userid,order_id=order_id,payment_id=payment_id,signature=signature,amount=amount,sellerid=sellerid)
            payment_history_obj.save()
            return JsonResponse({'status':'200'})

        except Exception as e:
            print(e)
            return JsonResponse({'status':'400'})