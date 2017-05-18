from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator, MaxValueValidator
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.utils import timezone
#from audit_log.models.fields import LastUserField, LastSessionKeyField
#from audit_log.models.managers import AuditLog
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.
def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

    # Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=50,default='',blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __unicode__(self): #Python 3.3 is__str__
        return self.email

class Crash(models.Model):
    Checkout = models.NullBooleanField(default=False,blank=True)
#    user = LastUserField()
    ID = models.AutoField(primary_key=True)
    PS_case = models.BigIntegerField(null=True)
    PS_Case_ID = models.CharField(max_length=20,null=True)
    DLD =  models.CharField(max_length=20,null=True, blank=True)
    Validated = models.CharField(max_length=20,null=True)
    Date = models.CharField(max_length=18, blank=True, null=True)
    Date_of_Crash =  models.DateTimeField( blank=True, null=True)
    County_Code = models.CharField(max_length=6,null=True, blank=True)
    Route = models.CharField(max_length=5,null=True, blank=True)
    Direction = models.CharField(max_length=1,null=True, blank=True)
    Milepoint = models.CharField(max_length=8,null=True, blank=True)
    Crash_Verified = models.NullBooleanField(default=False, blank=True)
    City = models.CharField(max_length=20,null=True, blank=True)
    Exit_Number = models.IntegerField(validators=[MaxValueValidator(999)], null=True,  blank=True)
    Type = models.CharField(max_length=2, null=True,blank=True)
    Ramp_ID = models.CharField(max_length=4,null=True, blank=True)
    Case_Number = models.CharField(max_length=20,null=True, blank=True)
    Crash_Severity = models.IntegerField(validators=[MaxValueValidator(89)],null=True,blank=True)
    Nearest_City = models.CharField(max_length=25,null=True, blank=True)
    Distance = models.IntegerField(validators=[MaxValueValidator(5000)], null=True, blank=True)
    Manner_Collision = models.CharField(max_length=2,null=True, blank=True)
    Main_Road_Name = models.CharField(max_length=30,null=True, blank=True)
    Road_Junction_Feature = models.IntegerField(validators=[MaxValueValidator(99)],null=True, blank=True)
    Road_Jurisdiction = models.IntegerField(validators=[MaxValueValidator(99)], null=True, blank=True)
    At_Intersection_With = models.CharField(max_length=25,null=True, blank=True)
    First_Harmful_Event = models.CharField(max_length=2,null=True, blank=True)
    Not_at_Intersection_Distance = models.CharField(max_length=8,null=True, blank=True)
    Not_at_Intersection_Direction = models.CharField(max_length=2,null=True, blank=True)
    Nearest_Intersection = models.CharField(max_length=25,null=True, blank=True)
    Ref_Post_Distance = models.CharField(max_length=8,null=True, blank=True)
    Ref_Post_Direction = models.CharField(max_length=2,null=True, blank=True)
    Ref_Post_Description = models.CharField(max_length=25,null=True, blank=True)
    Light_Condition = models.CharField(max_length=2,null=True, blank=True)
    Weather_Condition = models.CharField(max_length=2,null=True, blank=True)
    Road_Surface_Condition = models.CharField(max_length=2,null=True, blank=True)
    Work_Zone_Related = models.CharField(max_length=2,blank=True, null=True)
    Work_Zone_Worker_Present = models.CharField(max_length=2,blank=True, null=True)
    Work_Zone_ID = models.IntegerField(validators=[MaxValueValidator(99)], null=True, blank=True)
    Work_Zone_Location = models.IntegerField(validators=[MaxValueValidator(99)], null=True, blank=True)
    Unconfirmed_Fatality_Report = models.CharField(max_length=4,null=True)
    Narrative = models.TextField(null=True, blank=True)
    QC_Comments = models.TextField(null=True, blank=True)
    Motor_Carrier_Involved = models.CharField(max_length=1,null=True, blank=True)
    CMV_Verified = models.NullBooleanField(default=False, blank=True)
#    session = LastSessionKeyField()
    created_date = models.DateTimeField(null=True,
            default=timezone.now)
    published_date = models.DateTimeField(null=True,
            blank=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.PS_Case_ID

class Vehicle(models.Model):
    ID = models.AutoField(primary_key=True)
    PS_case = models.BigIntegerField()
    Vehicle_Number = models.IntegerField(null=True)
    Vin_Verified = models.CharField(max_length=2,null=True,blank=True)
    Vin =  models.CharField(max_length=40,null=True,blank=True)
    License_Plate_Number = models.CharField(max_length=15,null=True,blank=True )
    License_Plate_State = models.CharField(max_length=20,null=True,blank=True)
    Motor_Vehicle_Body_Type = models.CharField(max_length=2,null=True,blank=True)
    Trailing_Units = models.CharField(max_length=2,null=True,blank=True)
    Cargo_Body_Type = models.CharField(max_length=2,null=True,blank=True)
    Special_Function_Code = models.CharField(max_length=2,null=True,blank=True)
    First_Event = models.CharField(max_length=2,null=True,blank=True)
    Second_Event = models.CharField(max_length=2,null=True,blank=True)
    Third_Event = models.CharField(max_length=2,null=True,blank=True)
    Fourth_Event = models.CharField(max_length=2,null=True,blank=True)
    Roadway_Description = models.CharField(max_length=2,null=True,blank=True)
    Disposition_Of_Vehicle = models.CharField(max_length=20,null=True,blank=True)
    Towed_By = models.CharField(max_length=25,null=True,blank=True)
    Carrier_Name = models.CharField(max_length=64,null=True,blank=True)
    US_DOT_Number = models.CharField(max_length=15,null=True,blank=True)
    US_DOT_Verified = models.CharField(max_length=1,null=True,blank=True)
    GCWR_GVWR = models.CharField(max_length=2,null=True,blank=True)
    Carrier_Address_Street = models.CharField(max_length=40,null=True,blank=True)
    Carrier_Address_Street2 = models.CharField(max_length=40,null=True,blank=True)
    Carrier_Address_City = models.CharField(max_length=25,null=True,blank=True)
    Carrier_Address_State = models.CharField(max_length=2,null=True,blank=True)
    Carrier_Address_Zip = models.CharField(max_length=12,null=True,blank=True)
    Carrier_Address_County = models.CharField(max_length=3,null=True,blank=True)
    Carrier_Address_Phone = models.CharField(max_length=25,null=True,blank=True)
    Is_Driver_Carrier = models.CharField(max_length=1,null=True,blank=True)
    Interstate = models.CharField(max_length=1,null=True,blank=True)
    Cargo_Code = models.CharField(max_length=2,null=True,blank=True)
    Hazmat_Released = models.CharField(max_length=1,null=True,blank=True)
    Hazmat_Placard_Number = models.CharField(max_length=20,null=True,blank=True)
    Is_Owner_Driver = models.CharField(max_length=1,null=True,blank=True)
    Owner_First = models.CharField(max_length=20,null=True,blank=True)
    Owner_Middle = models.CharField(max_length=20,null=True,blank=True)
    Owner_Last = models.CharField(max_length=20,null= True,blank=True)
    Owner_Address_Street = models.CharField(max_length=40,null=True,blank=True)
    Owner_Address_Street2 = models.CharField(max_length=40,null=True,blank=True)
    Owner_Address_City = models.CharField(max_length=25,null=True,blank=True)
    Owner_Address_State = models.CharField(max_length=2,null=True,blank=True)
    Owner_Address_Zip = models.CharField(max_length=12,null=True,blank=True)
    Owner_Phone = models.CharField(max_length=25,null=True,blank=True)
    Vehicle_ID = models.IntegerField(null=True,blank=True)
    Make = models.CharField(max_length=15,null=True,blank=True)
    Vehicle_Model = models.CharField(max_length=15,null=True,blank=True)
    Travel_Direction = models.IntegerField(validators=[MaxValueValidator(99)], null=True)
    Vehicle_Maneuver = models.IntegerField(validators=[MaxValueValidator(99)], null=True)
    Traffic_Control_Device = models.IntegerField(validators=[MaxValueValidator(99)], null=True)
    Driver_Condition = models.IntegerField(validators=[MaxValueValidator(99)], null=True)
    created_date = models.DateTimeField(null=True,
            default=timezone.now)
    published_date = models.DateTimeField(null=True,
            blank=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.PS_case
    
class Person(models.Model):
#  title = models.CharField(max_length=200)
    ID = models.AutoField(primary_key=True)
    PS_case = models.BigIntegerField(null=True)
    Name_Last = models.CharField(max_length=25,null=True,blank=True)
    Name_First = models.CharField(max_length=25,null=True,blank=True)
    Name_Middle = models.CharField(max_length=25,null=True,blank=True)
    Sex = models.CharField(max_length=1,null=True, blank=True)
    Date_Of_Birth = models.CharField(max_length = 10, blank=True, null=True)
#   Date_Of_Birth1 = models.DateTimeField(blank=True, null=True)
    Age = models.IntegerField(validators=[MaxValueValidator(125)], null=True)
    Address_Street = models.CharField(max_length=40,null=True,blank=True)
    Address_Street2 = models.CharField(max_length=40,null=True,blank=True)
    Address_City = models.CharField(max_length=25,null=True,blank=True)
    Address_State = models.CharField(max_length=2,null=True,blank=True)
    Address_Zip = models.CharField(max_length=12,null=True,blank=True)
    Address_County = models.CharField(max_length=3, null=True,blank=True)
    Phone = models.CharField(max_length=25,null=True,blank=True)
    Dl_Number= models.CharField(max_length=25,null=True,blank=True)
    Dl_State = models.CharField(max_length=2,null=True,blank=True)
    Dl_Class = models.CharField(max_length=2,null=True,blank=True)
    CDL_Presented_At_Scene = models.IntegerField(null=True,blank=True)
    Transported_To = models.CharField(max_length=2,null=True,blank=True)
    Injury_Level = models.CharField(max_length=2,null=True,blank=True)
    Charge = models.CharField(max_length=64,null=True,blank=True)
    Status_Code = models.CharField(max_length=2,null=True,blank=True)
    Person_Type = models.IntegerField(validators=[MaxValueValidator(99)], null=True)
    Vehicle_Number = models.IntegerField(validators=[MaxValueValidator(88)], null=True)
    created_date = models.DateTimeField(default=timezone.now, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.ID

#class UPost(models.Model):
class uc(models.Model):
    ID = models.AutoField(primary_key=True)
    FK = models.BigIntegerField(null=True, blank=True)
    PS_case = models.BigIntegerField(null=True, blank=True)
    PS_Case_ID = models.CharField(max_length=20,null=True)
    DLD_Year = models.CharField(max_length=4,null=True, blank=True)
    DLD = models.CharField(max_length=20,null=True, blank=True)
    Date_of_Crash = models.DateField(null=True, blank=True)
    County_Code = models.CharField(max_length=3,null=True, blank=True)
    Route = models.CharField(max_length=4,null=True, blank=True)
    Manner_Collision = models.CharField(max_length=2,null=True, blank=True)
    Roadway_Contrib_Circum = models.CharField(max_length=2,null=True, blank=True)
    Weather_Condition = models.CharField(max_length=2,null=True, blank=True)
    First_Harmful_Event = models.CharField(max_length=2,null=True, blank=True)
    Narrative = models.TextField(null=True, blank=True)
    Total_Fatalities = models.IntegerField(validators=[MaxValueValidator(99)], null=True,blank=True)
    Assigned_Crash_Record = models.NullBooleanField(default=False, blank=True)
    QC_Comments = models.TextField(null=True, blank=True)
    published_date = models.DateTimeField( blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.ID

class uv(models.Model):
    ID = models.AutoField(primary_key=True)
    PS_case = models.BigIntegerField(null=True, blank=True)
    FK = models.BigIntegerField(null=True, blank=True)
    Prop = models.BigIntegerField(null=True, blank=True)
    Vehicle_Number = models.IntegerField(validators=[MaxValueValidator(88)], null=True, blank=True)
    MV_Body = models.IntegerField(validators=[MaxValueValidator(88)], null=True, blank=True)
    def __str__(self):
        return self.ID

class up(models.Model):
    ID = models.AutoField(primary_key=True)
    PS_case = models.BigIntegerField(null=True, blank=True)
    FK = models.BigIntegerField(null=True, blank=True)
    Prop = models.BigIntegerField(null=True, blank=True)
    Vehicle_Number = models.IntegerField(validators=[MaxValueValidator(88)], null=True, blank=True)
    Person_Type = models.IntegerField(validators=[MaxValueValidator(99)], null=True,blank=True)
    Safety_Equip = models.IntegerField(validators=[MaxValueValidator(99)], null=True, blank=True)
    State_Reside = models.IntegerField(validators=[MaxValueValidator(3)], null=True,blank=True)
    Sex = models.CharField(max_length=3,null=True,blank=True)
    Full_Name = models.CharField(max_length=75,null=True, blank=True)
    Age = models.IntegerField(validators=[MaxValueValidator(125)], null=True, blank=True) 
    def __str__(self):
        return self.ID


class Locate(models.Model):
    id = models.AutoField(primary_key=True)
    PS_Case_ID = models.CharField(max_length=20,null=True)
#    latitude = models.FloatField(null=True,blank=True)
#    longitude = models.FloatField(null=True,blank=True)
    latitude = models.CharField(max_length=22, null=True, blank=True)
    longitude = models.CharField(max_length=22, null=True, blank=True)
    milepoint = models.CharField(max_length=10,null=True,blank=True)
    route_number = models.CharField(max_length=11,null=True,blank=True)
    type_road = models.CharField(max_length=2, null=True, blank=True)
    direction = models.CharField(max_length=2, null=True)
    exit_number = models.CharField(max_length=3, null=True)
    ramp_ID = models.CharField(max_length=2, null=True)
    county_ID = models.CharField(max_length=10,null=True,blank=True)
    address = models.CharField(null=True,max_length=100,blank=True)
    city = models.CharField(max_length=30,null=True,blank=True)
    zip_code = models.CharField(max_length=10,null=True,blank=True)
    event_date = models.DateTimeField( blank=True, null=True)
    def __str__(self):
        return self.address
    @property
    def coordinates(self):
        return Point(self.longitude, self.latitude)
                                                                                                                                                                              
