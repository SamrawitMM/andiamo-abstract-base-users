from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import MyUser, Driver, Owner, Passenger
# from django.contrib.auth.models import MyUser

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'full_name', 'email', 'phone_number', 'profile_pic')

    def create(self, validated_data):
        user = Driver.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('id', 'full_name', 'email', 'phone_number', 'password')
    
    def create(self, validated_data):
        user = Owner.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
        
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ('id', 'full_name', 'email', 'phone_number', 'password', 'profile_pic')
    
    def create(self, validated_data):
        user = Passenger.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'full_name', 'email', 'phone_number',)
        extra_kwargs = {'password' : {'write_only' : True, 'required' : True}}

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
        # we are passing more information for the field password
        # write_only  we won't be able to see(it will be hidden to the GET) 
        # but we should set it(the value) when using POST 
        # required if we want to be registered