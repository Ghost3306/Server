from users.models import Cart,SaveLater
from rest_framework import serializers

class CartShowSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields = '__all__'

class SaveShowSerializer(serializers.ModelSerializer):
    class Meta:
        model=SaveLater
        fields='__all__'