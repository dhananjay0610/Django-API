from django.shortcuts import render
from rest_framework import viewsets
from api.models import Asset,TravelInfo,UserDetails
from api.serializers import AssetSerializer,TravelInfoSerializer,UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView

class AssetViewSet(viewsets.ModelViewSet):
    queryset=Asset.objects.all()
    serializer_class=AssetSerializer
        #asset/{Id}/traveler/
    @action(detail=True,methods=['get'])
    def travelers(self, request,pk=None):
        try:
            asset=Asset.objects.get(pk=pk) 
            query=Q(startlocation=asset.startlocation)
            query.add(Q(endlocation=asset.endlocation),Q.AND)
            travelinfos=TravelInfo.objects.filter(query) 
            traveler_serializer=TravelInfoSerializer(travelinfos,many=True,context={'request':request})
            return Response(traveler_serializer.data)
        except Exception as e:
            return Response({
                'message': "Traveler does not exist"
            })
    

class TravelInfoViewSet(viewsets.ModelViewSet):
    queryset=TravelInfo.objects.all()
    serializer_class=TravelInfoSerializer
    

class UserDetailViewSet(viewsets.ModelViewSet):
    queryset=UserDetails.objects.all()
    serializer_class=UserSerializer
     #register/{Id}/asset/
    @action(detail=True,methods=['get'])
    def assets(self, request,pk=None):
        try:
            userDetails=UserDetails.objects.get(pk=pk) 
            emps=Asset.objects.filter(UserName=userDetails)
            asset_serializer=AssetSerializer(emps,many=True,context={'request':request})
            return Response(asset_serializer.data)
        except Exception as e:
            return Response({
                'message': "This user does not have any assets"
            })