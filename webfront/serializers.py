from rest_framework import serializers
from webfront.models import LANGUAGE_CHOICES, STYLE_CHOICES, Crash, Vehicle, Person, Locate, uc, uv, up
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import filters
from rest_framework import generics
import json
ModelSerializer = serializers.HyperlinkedModelSerializer

#QC GROUP
class CrashSerializer(serializers.Serializer):
    ID = serializers.IntegerField()
    PS_Case_ID = serializers.CharField(required=False, allow_blank=True, max_length=100)
    Date_of_Crash = serializers.DateTimeField()
    Crash_Verified = serializers.NullBooleanField()
    City = serializers.CharField(required=False, allow_blank=True, max_length=100)
    Main_Road_Name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    Narrative = serializers.CharField(required=False, allow_blank=True, max_length=100)
    Checkout = serializers.BooleanField(required=False)
    def create(self, validated_data):
         """
         Create and return a new `Snippet` instance, given the validated data.
         """
         return Crash.objects.create(**validated_data)

    def update(self, instance, validated_data):
         """
         Update and return an existing `Snippet` instance, given the validated data.
         """
         instance.Date_of_Crash = validated_data.get('Date_of_Crash', instance.Date_of_Crash)
         instance.PS_Case_ID = validated_data.get('PS_Case_ID', instance.PS_case)
         instance.City = validated_data.get('City', instance.City )
         instance.Main_Road_Name = validated_data.get('Main_Road_Name', instance.Main_Road_Name )
         instance.Crash_Verified = validated_data.get('Crash_Verified', instance.Crash_Verified)
         instance.Narrative = validated_data.get('Narrative', instance.Narrative)
         instance.Checkout = validated_data.get('Checkout', instance.Checkout)
         instance.save() 
         return instance

class CrashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crash
        fields = ('ID','PS_Case_ID','Crash_Verified','Date_of_Crash','City','Main_Road_Name','Narrative','Checkout')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields =('ID','PS_case','Sex', 'Age', 'Injury_Level', 'Status_Code', 'Person_Type', 'Vehicle_Number')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('ID','PS_case','Vehicle_ID','Vehicle_Number','Make','Vehicle_Model', 'Travel_Direction','Vehicle_Maneuver','Traffic_Control_Device','Driver_Condition')


#UNCONFIRMED


class UCFCSerializer(serializers.Serializer):
    ID = serializers.IntegerField(read_only=True)
    PS_case = serializers.IntegerField(required=False)
    PS_Case_ID = serializers.CharField(required=False, allow_blank=True, max_length=100)
    Assigned_Crash_Record = serializers.NullBooleanField()
    DLD_Year = serializers.CharField(required=False, allow_blank=True, max_length=4)
    DLD  = serializers.CharField(required=False, allow_blank=True, max_length=20)
    Date_of_Crash = serializers.DateTimeField()
    County_Code = serializers.CharField(required=False, allow_blank=True, max_length=3)
    Route = serializers.CharField(required=False, allow_blank=True, max_length=4)
    Manner_Collision= serializers.CharField(required=False, allow_blank=True, max_length=2)
    Roadway_Contrib_Circum = serializers.CharField(required=False, allow_blank=True, max_length=2)
    Weather_Condition = serializers.CharField(required=False, allow_blank=True, max_length=2)
    First_Harmful_Event = serializers.CharField(required=False, allow_blank=True, max_length=2)
    Narrative = serializers.CharField(required=False, allow_blank=True, max_length=100)
    def create(self, validated_data):
         """
         Create and return a new `Snippet` instance, given the validated data.
         """
         return uc.objects.create(**validated_data)
     
    def update(self, instance, validated_data):
         """
         Update and return an existing `Snippet` instance, given the validated data.
         """
         instance.PS_case = validated_data.get('PS_case', instance.PS_case)
         instance.PS_Case_ID = validated_data.get('PS_Case_ID', instance.PS_case)
         instance.Assigned_Crash_Record = validated_data.get('Assigned_Crash_Record', instance.Assigned_Crash_Record)
         instance.DLD_Year = validated_data.get('DLD_Year', instance.DLD_Year)
         instance.DLD = validated_data.get('DLD', instance.DLD)
         instance.Date_of_Crash = validated_data.get('Date_of_Crash', instance.Date_of_Crash)
         instance.County_Code = validated_data.get('County_Code', instance.County_Code)
         instance.Route = validated_data.get('Route', instance.Route)
         instance.Manner_Collision = validated_data.get('Manner_Collision', instance.Manner_Collision)
         instance.Roadway_Contrib_Circum = validated_data.get('Roadway_Contrib_Circum', instance.Roadway_Contrib_Circum)
         instance.Weather_Condition = validated_data.get('Weather_Condition', instance.Weather_Condition)
         instance.First_Harmful_Event = validated_data.get('First_Harmful_Event', instance.First_Harmful_Event)
         instance.Narrative = validated_data.get('Narrative', instance.Narrative)
         instance.save()
         return instance
     
class UCFCSerializer(serializers.ModelSerializer):
    class Meta:
        model = uc
        fields = ('ID','PS_case','PS_Case_ID','Assigned_Crash_Record','DLD_Year', 'DLD', 'County_Code', 'Route', 'Date_of_Crash', 'Manner_Collision','Roadway_Contrib_Circum','Weather_Condition', 'First_Harmful_Event', 'Narrative')


class uvSerializer(serializers.Serializer):
    ID = serializers.IntegerField(read_only = True)
    FK = serializers.IntegerField(required=False)
    PS_case = serializers.IntegerField(required=False)
    Vehicle_Number = serializers.IntegerField(required=False)
    MV_Body = serializers.IntegerField(required=False)
    def create(self, validated_data):
         """
#        Create and return a new `Snippet` instance, given the validated data.
#        """
         return uv.objects.create(**validated_data)
    def update(self, instance, validated_data):
         """
#        Update and return an existing `Snippet` instance, given the validated data.
#        """
         instance.FK = validated_data.get('FK', instance.FK)
         instance.PS_case = validated_data.get('PS_case', instance.PS_case)
         instance.Vehicle_Number = validated_data.get('Vehicle_Number', instance.Vehicle_Number )
         instance.MV_Body = validated_data.get('MV_Body', instance.MV_Body )
         instance.save()
         return instance

class uvSerializer(serializers.ModelSerializer):
    class Meta:
        model = uv
        fields = ('ID','FK','PS_case','Vehicle_Number','MV_Body')

#GIS

class LocateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    PS_Case_ID = serializers.CharField(required=False, allow_blank=True, max_length=100)
    latitude = serializers.IntegerField(read_only=True)
    longitude = serializers.IntegerField(read_only=True)
    address = serializers.CharField(required=False, allow_blank=True, max_length=100)
    event_date =serializers.DateTimeField()
    city = serializers.CharField(required=False, allow_blank=True, max_length=100)
    zip_code  = serializers.CharField(required=False, allow_blank=True, max_length=100)
    def create(self, validated_data):
         """
         Create and return a new `Snippet` instance, given the validated data.
         """
         return Locate.objects.create(**validated_data)
    def update(self, instance, validated_data):
         """
         Update and return an existing `Snippet` instance, given the validated data.
         """
         instance.PS_Case_ID = validated_data.get('PS_Case_ID', instance.PS_Case_ID)
         instance.latitude = validated_data.get('latitude', instance.latitude)
         instance.longitude = validated_data.get('longitude', instance.logitude)
         instance.address = validated_data.get('address', instance.address )
         instance.city = validated_data.get('city', instance.city )
         instance.zip_code = validated_data.get('zip_code', instance.zip_code )
         instance.event_date = validated_data.get('event_date', instance.event_date )
         instance.save()
         return instance
     
class LocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locate
        fields = ('id','PS_Case_ID','latitude','longitude','milepoint','route_number','county_ID','address','city','zip_code', 'event_date')

class LocationSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """
    class Meta:
        model = Locate
        geo_field = "point"
        fields = ('id', 'PS_Case_ID','address', 'milepoint','route_number','county_ID','city', 'zip_code', 'event_date')
                                                                                                                                                                                                                                                   

#CMV GROUP

class CMVSerializer(serializers.Serializer):
    ID = serializers.IntegerField()
    PS_Case_ID = serializers.CharField(required=False, allow_blank=True, max_length=100)
    Date_of_Crash = serializers.DateTimeField()
    City = serializers.CharField(required=False, allow_blank=True, max_length=100)
    Main_Road_Name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    CMV_Verified = serializers.NullBooleanField()
    Checkout = serializers.BooleanField(required=False)
    def create(self, validated_data):
         """
         Create and return a new `Snippet` instance, given the validated data.
         """
         return Crash.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
         """
         Update and return an existing `Snippet` instance, given the validated data.
         """
         instance.Date_of_Crash = validated_data.get('Date_of_Crash', instance.Date_of_Crash)
         instance.PS_Case_ID = validated_data.get('PS_Case_ID', instance.PS_case)
         instance.City = validated_data.get('City', instance.City )
         instance.Main_Road_Name = validated_data.get('Main_Road_Name', instance.Main_Road_Name )
         instance.CMV_Verified = validated_data.get('Crash_Verified', instance.Crash_Verified)
         instance.Checkout = validated_data.get('Checkout', instance.Checkout)
         instance.save()
         return instance

class CMVSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crash
        fields = ('ID','PS_Case_ID','Date_of_Crash','City','Main_Road_Name','CMV_Verified','Checkout')


class CMVVSerializer(serializers.Serializer):
    ID  = serializers.IntegerField(read_only=True)
    PS_case = serializers.IntegerField(required=False)
    Carrier_Name = serializers.CharField(required=False, allow_blank=True, max_length=64)
    US_DOT_Number = serializers.CharField(required=False, allow_blank=True, max_length=15)
    US_DOT_Verified = serializers.CharField(required=False, allow_blank=True, max_length=1)
    GCWR_GVWR = serializers.CharField(required=False, allow_blank=True, max_length=2)
    Carrier_Address_Street = serializers.CharField(required=False, allow_blank=True, max_length=40)
    Carrier_Address_City = serializers.CharField(required=False, allow_blank=True, max_length=25)
    Carrier_Address_State = serializers.CharField(required=False, allow_blank=True, max_length=2)
    Carrier_Address_Zip = serializers.CharField(required=False, allow_blank=True, max_length=12)
    Carrier_Address_Phone = serializers.CharField(required=False, allow_blank=True, max_length=25)
    Is_Owner_Driver = serializers.CharField(required=False, allow_blank=True, max_length=1)
    Interstate = serializers.CharField(required=False, allow_blank=True, max_length=1)
    Cargo_Code = serializers.CharField(required=False, allow_blank=True, max_length=2)
    Hazmat_Placard_Number = serializers.CharField(required=False, allow_blank=True, max_length=20)
    Hazmat_Released = serializers.CharField(required=False, allow_blank=True, max_length=1)
    Owner_First = serializers.CharField(required=False, allow_blank=True, max_length=20)
    Owner_Middle = serializers.CharField(required=False, allow_blank=True, max_length=20)
    Owner_Last = serializers.CharField(required=False, allow_blank=True, max_length=20)
    Owner_Address_Street = serializers.CharField(required=False, allow_blank=True, max_length=40)
    Owner_Address_City = serializers.CharField(required=False, allow_blank=True, max_length=25)
    Owner_Address_State = serializers.CharField(required=False, allow_blank=True, max_length=2)
    Owner_Address_Zip = serializers.CharField(required=False, allow_blank=True, max_length=12)
    Owner_Phone = serializers.CharField(required=False, allow_blank=True, max_length=25)
    def create(self, validated_data):
         """
         Create and return a new `Snippet` instance, given the validated data.
         """
         return Vehicle.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
         """
         Update and return an existing `Snippet` instance, given the validated data.
         """
         instance.PS_case = validated_data.get('PS_case', instance.PS_case)
         instance.Carrier_Name = validated_data.get('Carrier_Name', instance.Carrier_Name )
         instance.US_DOT_Number = validated_data.get('US_DOT_Number', instance.US_DOT_Number )
         instance.US_DOT_Verified = validated_data.get('US_DOT_Verified', instance.US_DOT_Verified )
         instance.GCWR_GVWR = validated_data.get('GCWR_GVWR', instance.GCWR_GVWR )
         instance.Carrier_Address_Street = validated_data.get('Carrier_Address_Street', instance.Carrier_Address_Street )
         instance.Carrier_Address_City = validated_data.get('Carrier_Address_City', instance.Carrier_Address_City )
         instance.Carrier_Address_State = validated_data.get('Carrier_Address_State', instance.Carrier_Address_State )
         instance.Carrier_Address_Zip = validated_data.get('Carrier_Address_Zip', instance.Carrier_Address_Zip )
         instance.Carrier_Address_Phone = validated_data.get('Carrier_Address_Phone', instance.Carrier_Address_Phone )
         instance.Is_Owner_Driver = validated_data.get('Is_Owner_Driver', instance.Is_Owner_Driver )
         instance.Interstate = validated_data.get('Interstate', instance.Interstate )
         instance.Cargo_Code = validated_data.get('Cargo_Code', instance.Cargo_Code )
         instance.Hazmat_Placard_Number = validated_data.get('Hazmat_Placard_Number', instance.Hazmat_Placard_Number) 
         instance.Hazmat_Released = validated_data.get('Hazmat_Released', instance.Hazmat_Released )
         instance.Owner_First = validated_data.get('Owner_First', instance.Owner_First) 
         instance.Owner_Middle = validated_data.get('Owner_Middle', instance.Owner_Middle )
         instance.Owner_Last = validated_data.get('Owner_Last', instance.Owner_Last )
         instance.Owner_Address_Street = validated_data.get('Owner_Address_Street', instance.Owner_Address_Street) 
         instance.Owner_Address_City = validated_data.get('Owner_Address_City', instance.Owner_Address_City )
         instance.Owner_Address_State = validated_data.get('Owner_Address_State', instance.Owner_Address_State )
         instance.Owner_Address_Zip = validated_data.get('Owner_Address_Zip', instance.Owner_Address_Zip )
         instance.Owner_Phone = validated_data.get('Owner_Phone', instance.Owner_Phone )
         instance.save()
         return instance

class CMVVSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields =('ID','PS_case','Carrier_Name','US_DOT_Number','US_DOT_Verified','GCWR_GVWR','Carrier_Address_Street','Carrier_Address_City','Carrier_Address_State','Carrier_Address_Zip','Carrier_Address_Phone',
                 'Is_Owner_Driver','Interstate','Cargo_Code','Hazmat_Placard_Number','Hazmat_Released','Owner_First','Owner_Middle','Owner_Last','Owner_Address_Street','Owner_Address_City','Owner_Address_State',
                 'Owner_Address_Zip','Owner_Phone')

#STREAM
class PostSerializer(serializers.Serializer):
       ID = serializers.IntegerField()
       PS_case = serializers.IntegerField(required=False)
       Road_Junction_Feature = serializers.IntegerField(required=False)
       Work_Zone_Related = serializers.BooleanField(required=False)
       Work_Zone_Worker_Present = serializers.BooleanField(required=False)
       Work_Zone_ID = serializers.IntegerField(required=False)
       First_harmful_Event = serializers.IntegerField(required=False)
       Crash_Severity = serializers.IntegerField()
       Date_of_Crash = serializers.DateTimeField()
       City = serializers.CharField(required=False, allow_blank=True, max_length=100)
       Manner_Collision = serializers.CharField(required=False, allow_blank=True, max_length=100)
       def create(self, validated_data):
            """
            Create and return a new `Snippet` instance, given the validated data.
            """
            return Crash.objects.create(**validated_data)
        
       def update(self, instance, validated_data):
            """
            Update and return an existing `Snippet` instance, given the validated data.
            """
            instance.PS_case = validated_data.get('PS_case', instance.PS_case)
            instance.Road_Junction_Feature = validated_data.get('Road_Junction_Feature', instance.Road_Junction_Feature)
            instance.Work_Zone_Related = validated_data.get('Work_Zone_Related', instance.Work_Zone_Related)
            instance.Work_Zone_Worker_Present = validated_data.get('Work_Zone_Worker_Present', instance.Work_zone_Worker_Present)
            instance.Work_Zone_ID = validated_data.get('Work_Zone_ID', instance.Work_Zone_ID)
            instance.First_Harmful_Event = validated_data.get('First_Harmful_Event', instance.First_Harmful_Event)
            instance.Date_of_Crash = validated_data.get('Date_of_Crash', instance.Date_of_Crash)
            instance.Crash_Severity = validated_data.get('Crash_Severity', instance.Crash_Severity)
            instance.City = validated_data.get('City', instance.City )
            instance.Manner_Collision = validated_data.get('Manner_Collision', instance.Manner_Collision)
            instance.save()
            return instance
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crash
        fields = ('ID','PS_case','Road_Junction_Feature', 'Work_Zone_Related','Work_Zone_Worker_Present','Work_Zone_ID','First_Harmful_Event','Crash_Severity','Date_of_Crash','Date_of_Crash','City','Manner_Collision')


class ProfileSerializer(serializers.Serializer):
    ID  = serializers.IntegerField(read_only=True)
    FK = serializers.IntegerField(required=False)
    PS_case = serializers.IntegerField(required=False)
    Vehicle_Number = serializers.IntegerField(required=False)
    Person_Type = serializers.IntegerField(required=False)
    Safety_Equip = serializers.IntegerField(required=False)
    State_Reside  = serializers.IntegerField(required=False)
    Sex = serializers.CharField(required=False, allow_blank=True, max_length=3)
    Full_Name  = serializers.CharField(required=False, allow_blank=True, max_length=75)
    Age = serializers.IntegerField(required=False)
    def create(self, validated_data):
         """
         Create and return a new `Snippet` instance, given the validated data.
         """
         return up.objects.create(**validated_data)
     
    def update(self, instance, validated_data):
         """
         Update and return an existing `Snippet` instance, given the validated data.
         """
         instance.FK = validated_data.get('FK', instance.FK )
         instance.PS_case = validated_data.get('PS_case', instance.PS_case)
         instance.Vehicle_Number = validated_data.get('Vehicle_Number', instance.Vehicle_Number )
         instance.Person_Type  = validated_data.get('Person_Type', instance.Person_Type )
         instance.Safety_Equip = validated_data.get('Safety_Equip', instance.Safety_Equip )
         instance.State_Reside = validated_data.get('State_Reside', instance.State_Reside )
         instance.Sex = validated_data.get('Sex', instance.Sex )
         instance.Full_Name = validated_data.get('Full_Name', instance.Full_Name )
         instance.Age = validated_data.get('Age', instance.Age )
         instance.save()
         return instance
     
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = up
        fields =('ID','FK','PS_case','Vehicle_Number','Person_Type','Safety_Equip','State_Reside','Sex','Full_Name','Age')

