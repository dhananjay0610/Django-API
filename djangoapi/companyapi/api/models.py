from django.db import models

class UserDetails(models.Model):
    user_id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return self.firstname + ' '+ self.lastname

#Asset Model 
class Asset(models.Model):
    asset_id=models.AutoField(primary_key=True)
    startlocation=models.CharField(max_length=50)
    endlocation=models.CharField(max_length=50)
    dateTime=models.DateTimeField()
    noOfAsset=models.IntegerField()
    assetType=models.CharField(max_length=50,choices=(
        ('LAPTOP','LAPTOP'),
        ('TRAVEL_BAG','TRAVEL_BAG'),
        ('PACKAGE','PACKAGE')
    ))
    assetSensitivity=models.CharField(max_length=50,choices=(
        ('HIGHLY_SENSITIVE','HIGHLY_SENSITIVE'),
        ('SENSITIVE','SENSITIVE'),
        ('NORMAL','NORMAL')
    ))
    delivery=models.CharField(max_length=50)
    UserName=models.ForeignKey(UserDetails,on_delete=models.CASCADE,default=1)


#Traveler Model 
class TravelInfo(models.Model):
    traveler_id=models.AutoField(primary_key=True)
    startlocation=models.CharField(max_length=50)
    endlocation=models.CharField(max_length=50)
    dateTime=models.DateTimeField()
    travel_medium=models.CharField(max_length=50,choices=(
        ('BUS','BUS'),
        ('CAR','CAR'),
        ('TRAIN','TRAIN')
    ))