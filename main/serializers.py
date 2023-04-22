from rest_framework import serializers
from .models import Shoe

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = ['id', 'gender','model_name', 'color', 'size', 'price', 'material', 'style', 'description', 'photo']

