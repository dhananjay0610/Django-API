from rest_framework import serializers
from api.models import Asset,TravelInfo,UserDetails
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model= Asset
        fields= "__all__"


class TravelInfoSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model= TravelInfo
        fields= "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_id=serializers.ReadOnlyField()
    class Meta:
        model= UserDetails
        fields= "__all__"