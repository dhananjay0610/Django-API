from django.contrib import admin
from django.urls import path,include
from api.views import AssetViewSet,TravelInfoViewSet,UserDetailViewSet
from rest_framework import routers

router =routers.DefaultRouter()
router.register(r'asset',AssetViewSet)
router.register(r'traveler',TravelInfoViewSet)
router.register(r'register',UserDetailViewSet)
urlpatterns = [
    path('',include(router.urls)),
 ]