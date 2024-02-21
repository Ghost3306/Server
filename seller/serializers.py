from seller.models import Seller,SellerBanner
from rest_framework import serializers

class SellerShowSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields = '__all__'

class SellerBannerShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerBanner
        fields = '__all__'