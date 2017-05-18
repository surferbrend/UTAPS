from django import forms
from django.forms import ValidationError
from .models import SignUp, Vehicle, Person, Crash, uc, up, uv, Locate


#QC GROUP

class MC(forms.ModelForm):
    class Meta:
        model = Crash
        fields = ['ID','PS_case','DLD','Date','Route','Type','Direction','County_Code','Milepoint','City','Exit_Number',
                  'Ramp_ID','Case_Number','Crash_Severity','Nearest_City','Distance','Manner_Collision','Main_Road_Name',
                  'Road_Junction_Feature','Road_Jurisdiction', 'At_Intersection_With','First_Harmful_Event','Not_at_Intersection_Distance',
                  'Not_at_Intersection_Direction','Nearest_Intersection','Ref_Post_Distance','Ref_Post_Direction',
                  'Ref_Post_Description', 'Work_Zone_Location','Work_Zone_ID','Work_Zone_Related','Work_Zone_Worker_Present','Narrative','QC_Comments','Crash_Verified']

class Check(forms.ModelForm):
    class Meta:
        model = Crash
        fields = ['ID','PS_case','Checkout']


class MV(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['ID','PS_case','Vehicle_ID','Vehicle_Number','Make','Vehicle_Model','Travel_Direction',
                  'Vehicle_Maneuver','Traffic_Control_Device','Driver_Condition',]
                                                                
class MP(forms.ModelForm):
    class Meta:
        model = Person
        fields =['ID', 'PS_case','Vehicle_Number','Name_First','Name_Middle','Name_Last','Person_Type','Sex','Date_Of_Birth','Age','Injury_Level']

# UNCONFIRMED

class uvForm(forms.ModelForm):
    class Meta:
        model = uv
        fields = ['ID','Vehicle_Number','MV_Body']

class upForm(forms.ModelForm):
    class Meta:
        model = up
        fields =['ID','Vehicle_Number','Person_Type','Safety_Equip','State_Reside','Sex','Full_Name','Age']

class ucForm(forms.ModelForm):
    class Meta:
        model = uc
        fields = ['ID','FK','PS_case','DLD_Year', 'DLD', 'County_Code', 'Route', 'Date_of_Crash', 'Manner_Collision','Roadway_Contrib_Circum',
                  'Weather_Condition', 'First_Harmful_Event', 'Narrative', 'Total_Fatalities','Assigned_Crash_Record','QC_Comments']


#GIS        

class cap(forms.ModelForm):
    class Meta:
        model = Locate
        fields = ['id','PS_Case_ID','latitude','longitude','milepoint','route_number','county_ID','address','city','zip_code']

class V(forms.ModelForm):
    class Meta: 
        model = Crash
        fields = ['ID','PS_case','Route','County_Code','Milepoint','City','Main_Road_Name']

#HOOKS
class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()
    def clean_email(self): #Validation fields or methods
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extention = provider.split('.')
        if not extention  == "edu":
            raise forms.ValidationError("Please use a valid .edu email address")
        return email

class SignUpForm(forms.models.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email']
        def clean_email(self): #Validation fields or methods
            email = self.cleaned_data.get('email') 
            email_base, provider = email.split("@")
            domain, extention = provider.split('.')
            if not extention  == "edu":
                raise forms.ValidationError("Please use a valid .edu email address")
            return email
        

        def clean_fullname(self):
            full_name =self.clean_data.get('full_name')
            return full_name

