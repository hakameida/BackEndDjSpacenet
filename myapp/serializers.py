from rest_framework import serializers
from .models import Laptop
from .models import Product




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
