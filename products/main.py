from django.conf import settings
from django.core.mail import  send_mail
from users.models import Customers
def send_dispatch_mail( product_name, quantity, price, order_number, tracking_number, courier_service,sellername,uuid,delcharge):
    from_email = settings.EMAIL_HOST_USER
    print('sending mail')
    user = Customers.objects.filter(apikey=uuid)
    cust_main = ''
    cust_name =''
    total = (price*quantity)+delcharge 
    for x in user:
        cust_main = x.email
        cust_name = x.name
        break
    subject = 'Notification: Your Parcel Has Been Dispatched'
    message = f'''Dear {cust_name},

    We are pleased to inform you that your order with {sellername} has been successfully processed and dispatched to our trusted courier service for delivery. Your parcel is now en route to you.

    Here are the details of your shipment:
    Product Name: {product_name}
    Price: {price}
    Quantity: {quantity}
    Subtotal: {total}
    Order Number: {order_number}
    Tracking Number: {tracking_number}
    Courier Service: {courier_service}

    You can track the progress of your delivery using the provided tracking number on the courier service's website.

    If you have any inquiries or concerns regarding your order or delivery, please do not hesitate to contact us. Our dedicated customer support team is here to assist you.

    Thank you for choosing {sellername}. We greatly value your business and trust that you will enjoy your purchase.

    Kind regards,
    Lalit Rawool
    Online Bazaarpeth
    '''
    


    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, [cust_main,])
            print('mail send successfully')
            return {'status':'200','message':'otp send successfully...'}
        except Exception as e:
            print(e)
            return {'status':'500','message':e,}
        
    else:    
        return {'status':'400','message':'Invalid email address....Please reenter email!',}

# send_dispatch_mail('customer_name', 'product_name', 'quantity', 'price', 'order_number', 'tracking_number', 'courier_service','sellername','bf927fa687753ce6aa1e38e77009cb81')