from products.models import Products,PlacedOrder,Review
from rest_framework import serializers

class ProductsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields = '__all__'


class PlaceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlacedOrder
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'