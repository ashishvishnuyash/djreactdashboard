from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        
        # def create(self, validated_data):
        #     user = User.objects.create_user(validated_data['username'])
        #     user.set_password(validated_data['password'])
        #     user.save()
        #     return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'color', 'catagory']