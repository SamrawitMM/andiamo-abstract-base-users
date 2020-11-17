from django.shortcuts import render

from django.shortcuts import render
from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import MyUser, Driver, Passenger, Owner
from .serializers import MyUserSerializer, DriverSerializer, PassengerSerializer, OwnerSerializer
# from django.contrib.auth.models import User
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
# from .serializer import RegisterSerializer
# from django.contrib.auth.models import User


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (AllowAny, )
class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class RegisterApi(generics.GenericAPIView):
    serializer_class = PassengerSerializer

    @classmethod
    def get_extra_actions(cls):
        return []


    # def post(self, request, *args,  **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #     return Response({
    #         "user": PassengerSerializer(user, context=self.get_serializer_context()).data,
    #         "message": "User Created Successfully.  Now perform Login to get your token",
    #     })