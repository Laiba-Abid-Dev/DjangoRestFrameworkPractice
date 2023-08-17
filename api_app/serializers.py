from rest_framework import serializers
from .models import CartItem


class CartSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)
    price = serializers.IntegerField()
    quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CartItem
        fields = ('__all__')

