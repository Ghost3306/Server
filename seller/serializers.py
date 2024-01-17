from seller.models import Seller
from rest_framework import serializers

class SellerShowSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields = '__all__'
