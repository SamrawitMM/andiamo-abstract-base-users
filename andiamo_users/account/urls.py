from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('myuser', views.MyUserViewSet)
router.register('driver', views.DriverViewSet)
router.register('passenger', views.PassengerViewSet)
router.register('owner', views.OwnerViewSet)







urlpatterns = [
   path('', include(router.urls))
]