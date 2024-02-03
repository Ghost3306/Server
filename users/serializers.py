from users.models import Cart
from rest_framework import serializers

class CartShowSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields = '__all__'