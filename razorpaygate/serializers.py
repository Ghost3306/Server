from rest_framework import serializers
from razorpaygate.models import PaymentHistory

class HistoryPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        Model=PaymentHistory
        fields='__all__'
