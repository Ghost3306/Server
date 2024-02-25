from django.contrib import admin

from razorpaygate.models import PaymentHistory
from razorpaygate.serializers import HistoryPaymentSerializer

class DisplayPaymentHistory(admin.ModelAdmin):
    list_display = ('sellerid','userid','payment_id','order_id','signature','amount','datetime')

admin.site.register(PaymentHistory,DisplayPaymentHistory)

