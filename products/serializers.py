from products.models import Products
from rest_framework import serializers

class ProductsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields = '__all__'