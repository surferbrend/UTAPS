from django.shortcuts import render
from django import template
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.core import serializers
from django.core.urlresolvers import reverse
from .forms import ContactForm, SignUpForm, Vehicle, Person, MC, MV, MP, ucForm ,upForm, uvForm, uc, Check, V, cap
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import SignUp, Vehicle, Person, Locate, Crash, uc, uv, up
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import permissions, renderers, viewsets, generics, filters, status
from rest_framework.decorators import detail_route, api_view
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import PostSerializer, LocateSerializer, PersonSerializer, CMVVSerializer, VehicleSerializer, CrashSerializer, LocationSerializer, UCFCSerializer, uvSerializer, ProfileSerializer, CMVSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import logging, json, re, time

# Create your views here.
#Main Views

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html",{})

def form(request):
    return render(request, "forms.html", {})

def contact(request):
    title = 'Contact Us'
    title_align_center = True
    form =ContactForm(request.POST or None)
    if form.is_valid():
        form_email =form.cleaned_data.get("email")
        form_message =form.cleaned_data.get("message")
        form_full_name =form.cleaned_data.get("full_name")
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email= [from_email,'juan.c.medina@utah.edu']
        contact_message = " %s: %s via %s"%(
                form_full_name,
                form_message,
                form_email)
        send_mail(subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=True)
        context ={
                "form": form,
                "title": title,
                "title_align_center": title_align_center,
                }
        return render(request, "forms.html", context)


@login_required
#@duo_auth.duo_auth_required
def profile(request):
    return render(request, "profile.html", {})

@login_required
#@duo_auth.duo_auth_required
def dyno(request):
    return render(request, 'dyno.html', {})

@login_required
#@duo_auth.duo_auth_required
def full(request):
    return render(request, 'full.html', {})

@login_required
#@duo_auth.duo_auth_required
def u(request):
    return render(request, 'dyna.html', {})

@login_required
#@duo_auth.duo_auth_required
def full(request):
    return render(request, 'full.html', {})


##QC GROUP

def crash_detail(request, pk):
    post = get_object_or_404(Crash, pk=pk)
    return render(request, 'crash_detail.html', {'post': post})

#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def crash_new(request):
    args = {}
    args.update(csrf(request))
    if request.method == "POST":
       form = MC(request.POST)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.published_date = timezone.now()
           post.save()
           return redirect('crash_detail', pk=post.pk)
    else:
         form = MC()
   # return render(request, 'sub1.html', {'form': form})
    return render(request, 'crash_edit.html', {'form': form})

#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def crash_edit(request, pk):
    args = {}
    args.update(csrf(request))
    post = get_object_or_404(Crash, pk=pk)
    user = request.user
    if request.method == "POST":
       form = MC(request.POST, instance=post)
       if form.is_valid():
           post = form.save(commit=False)
           post.user = request.user
           post.published_date = timezone.now()
           post.save()
           return redirect('crash_edit', pk=post.pk)
    else:
         form = MC(instance=post)
         data = form['PS_case'].value()
         request.session['dump']= post.pk
         request.session['dd'] = data
         queryset = Vehicle.objects.all().filter(PS_case__exact = data)
         queryset2 = Person.objects.all().filter(PS_case__exact = data)
         queryset3 = uc.objects.all().filter(PS_case__exact = data)
         queryset4 = Locate.objects.all().filter(PS_Case_ID = data)
#         que = Crash.objects.all().filter(Checkout__exact = 2)
         context = {
         "queryset":queryset,
         "queryset2":queryset2,
         "queryset3":queryset3,
         "queryset4":queryset4,
#         "que":que,
         "data": data,
         "form": form
         }
    return render(request, 'crash_edit.html', context)


#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def check_new(request):
    args = {}
    args.update(csrf(request))
    if request.method == "POST":
       form = Check(request.POST)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.published_date = timezone.now()
           post.save()
           return redirect('crash_edit', pk=post.pk)
    else:
         form = Check()
    return render(request, 'form-edit.html', {'form': form})

#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def crash_check(request, pk):
    args = {}
    args.update(csrf(request))
    post = get_object_or_404(Crash, pk=pk)
    user = request.user
    if request.method == "POST":
       form = Check(request.POST, instance=post)
       if form.is_valid():
           post = form.save(commit=False)
           post.user = request.user
           post.published_date = timezone.now()
           post.save()
           return redirect('crash_edit', pk=post.pk)
    else:
         form = Check(instance=post)
         data = form['PS_case'].value()
         context = {
         "data": data,
         "form": form,
         }
    return render(request, 'checkout.html', context)

#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def checkin(request, pk):
    args = {}
    args.update(csrf(request))
    post = get_object_or_404(Crash, pk=pk)
    user = request.user
    if request.method == "POST":
       form = Check(request.POST, instance=post)
       if form.is_valid():
           post = form.save(commit=False)
           post.user = request.user
           post.published_date = timezone.now()
           post.save()
           return redirect('search')
    else:
         form = Check(instance=post)
         data = form['PS_case'].value()
         context = {
         "data": data,
         "form": form,
         }
    return render(request, 'checkout.html', context)


def person_detail(request, pk):
    post = get_object_or_404(Person, pk=pk)
    return render(request, 'person_detail.html', {'post': post})

#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def person_new(request):
    args = {}
    args.update(csrf(request))
    if request.method == "POST":
       form = MP(request.POST)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.published_date = timezone.now()
           post.save()
           return redirect('person_detail', pk=post.pk)
    else:
        form = MP()
    return render(request, 'form-edit.html', {'form': form})

#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def person_edit(request, pk):
    args = {}
    args.update(csrf(request))
    post = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
       form = MP(request.POST, instance=post)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.published_date = timezone.now()
           post.save()
           return redirect('person_edit', pk=post.pk)
    else:
        form = MP(instance=post)
    return render(request, 'form-edit.html', {'form': form})


def vehicle_detail(request, pk):
    post = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicle_detail.html', {'post': post})
        
#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def vehicle_new(request):
    args = {}
    args.update(csrf(request))
    if request.method == "POST":
        form = MV(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('vehicle_detail', pk=post.pk)
    else:
        form = MV()
    return render(request, 'form-edit.html', {'form': form})

#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def vehicle_edit(request, pk):
    args = {}
    args.update(csrf(request))
    post = get_object_or_404(Vehicle, pk=pk)
    if request.method == "POST":
         form = MV(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('vehicle_edit', pk=post.pk)
    else:
        form = MV(instance=post)
    return render(request, 'form-edit.html', {'form': form})

#UNCONFIRMED

#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def uc_new(request):
    args = {}
    args.update(csrf(request))
    if request.method == "POST":
         form = ucForm(request.POST)
         if form.is_valid():
              post = form.save(commit=False)
              post.author = request.user
              post.published_date = timezone.now()
              post.FK = post.pk
              post.save()
              return redirect('uc-edit', pk=post.pk)
    else:
        form = ucForm()
        context = {
        "form":form
        }
    return render(request, 'sub4.html',context)
                                                                                                                                
#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def uc_edit(request, pk):
    args = {}
    args.update(csrf(request))
    post = get_object_or_404(uc, pk=pk)
    if request.method == "POST":
         form = ucForm(request.POST, instance=post)
         if form.is_valid():
               post = form.save(commit=False)
               post.author = request.user
               post.published_date = timezone.now()
               post.save()
               return redirect('uc-edit', pk=post.pk)
    else:
        form = ucForm(instance=post)
        data = form['FK'].value()
        request.session['pstemp']= data
        request.session['del']= post.pk
        queryset = uv.objects.all().filter(FK__exact = data)
        queryset2 = up.objects.all().filter(FK__exact = data)
        context = {
        "queryset":queryset,
        "queryset2":queryset2,
        "data": data,
        "form": form
        }
    return render(request, 'sub.html', context)


#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def uce(request, pk):
    args = {}
    args.update(csrf(request))
    post = get_object_or_404(uc, pk=pk)
    if request.method == "POST":
        form = ucForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('uce', pk=post.pk)
    else:
        form = ucForm(instance=post)
        data = form['FK'].value()
        queryset = uv.objects.all().filter(FK__exact = data)
        queryset2 = up.objects.all().filter(FK__exact = data)
        context = {
        "queryset":queryset,
        "queryset2":queryset2,
        "data": data,
        "form": form
        }
    return render(request, 'uce.html', context)

#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def uv_new(request):
    args = {}
    args.update(csrf(request))
    if request.method == "POST":
        aa = request.session['pstemp']
        form = uvForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.FK = aa
            post.published_date = timezone.now()
            post.save()
            return redirect('uv-detail', pk=aa)
        else:
            form = uvForm()
        return render(request, 'sub1.html', {'form': form})

#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def up_new(request):
    args = {}
    args.update(csrf(request))
    if request.method == "POST":
        aa = request.session['pstemp']
        form = upForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.FK = aa
            post.published_date = timezone.now()
            post.save()
            return redirect('up-detail', pk=aa)
        else:
            form = upForm()
        return render(request, 'sub1.html', {'form': form})

#GIS

#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def geo_new(request):
    args = {}
    args.update(csrf(request))
    if request.method == "POST":
        form = cap(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('geo-edit', pk=post.pk)
    else:
        form = cap()
        context = {
        "form":form
        }
    return render(request, 'sub1.html', context)

#@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def geo_edit(request, pk):
    args = {}
    args.update(csrf(request))
    post = get_object_or_404(Locate, pk=pk)
    user = request.user
    request.session['geo']= post.pk
    if request.method == "POST":
       form = cap(request.POST, instance=post)
       if form.is_valid():
           post = form.save(commit=False)
           post.user = request.user
           post.published_date = timezone.now()
           post.save()
           return redirect('geo-edit', pk=post.pk)
    else:
        form = cap(instance=post)
        data = form['PS_Case_ID'].value()
        queryset = Locate.objects.all().filter(PS_Case_ID = data)
        context = {
        "queryset":queryset,
        "data": data,
        "form": form
        }
    return render(request, 'record.html', context)


##REST_FRAMEWORK
class CrashListView(viewsets.ReadOnlyModelViewSet):
     queryset = Crash.objects.all()
     serializer_class = PostSerializer
     paginate_by = 20
     paginate_by_peram = 'page_size'
     filter_backends = (filters.SearchFilter,)
     search_fields = ('ID','PS_case','Road_Junction_Feature', 'Work_Zone_Related','Work_Zone_Worker_Present','Work_Zone_ID','First_Harmful_Event','Crash_Severity','Date_of_Crash','Date_of_Crash','City','Manner_Collision')

class CrashViewSet(viewsets.ReadOnlyModelViewSet):
     queryset = Crash.objects.all()
     serializer_class = CrashSerializer
     filter_backends = (filters.DjangoFilterBackend,)
     filter_fields = ('PS_case','Date_of_Crash', 'City','Main_Road_Name',)

class PViewset(viewsets.ModelViewSet):
     queryset = Person.objects.all()
     serializer_class = PersonSerializer
     filter_backends = (filters.DjangoFilterBackend,)
     filter_fields = ('ID','PS_case','Sex', 'Age', 'Injury_Level', 'Status_Code', 'Person_Type','Vehicle_Number')


class ProfileDetail(APIView):
     renderer_classes = [TemplateHTMLRenderer]
     template_name = 'profile_detail.html'

     def get(self, request, pk):
         profile = get_object_or_404(up, pk=pk)
         serializer = ProfileSerializer(profile)
         return Response({'serializer': serializer, 'profile': profile})

     def post(self, request, pk):
         profile = get_object_or_404(up, pk=pk)
         serializer = ProfileSerializer(profile, data=request.data)
         if not serializer.is_valid():
              return Response({'serializer': serializer, 'profile': profile})
         serializer.save()
         return redirect('profile_list.html')

def serialize_queryset(self, serializer_class, queryset):
    self.serializer_class = serializer_class#api_serializers.EntitlementDetailSerializer
    self.paginate_by = None
    self.object_list = queryset
    page = self.paginate_queryset(self.object_list)
    if page is not None:
        serializer = self.get_pagination_serializer(page)
    else:
        serializer = self.get_serializer(self.object_list, many=True)
    return Response(serializer.data)

class LocationList(generics.ListCreateAPIView):
    model = Locate
    serializer_class = LocationSerializer
    queryset = Locate.objects.all()

location_list = LocationList.as_view()


class LocationDetails(generics.RetrieveUpdateDestroyAPIView):
    model = Locate
    serializer_class = LocationSerializer
    queryset = Locate.objects.all()

location_details = LocationDetails.as_view()

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Crash.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('PS_case','Date_of_Crash', 'City','Main_Road_Name',)

#@login_required
#@duo_auth.duo_auth_required
class ListView(viewsets.ModelViewSet):
    queryset = Crash.objects.all()
    serializer_class = CrashSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('PS_Case_ID','Date_of_Crash', 'Crash_Verified','City','Main_Road_Name','Narrative','Checkout')

class CMVView(viewsets.ModelViewSet):
    queryset = Crash.objects.all()
    serializer_class = CMVSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('PS_Case_ID','Date_of_Crash', 'City','Main_Road_Name','CMV_Verified','Checkout')

#@login_required
#@duo_auth.duo_auth_required

class PostListView(viewsets.ReadOnlyModelViewSet):
    queryset = Crash.objects.all()
    serializer_class = PostSerializer
    paginator = None
    paginate_by = 20
    paginate_by_peram = 'page_size'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('ID','PS_case','Road_Junction_Feature', 'Work_Zone_Related','Work_Zone_Worker_Present','Work_Zone_ID','First_Harmful_Event','Crash_Severity','Date_of_Crash','Date_of_Crash','City','Manner_Collision')

#@login_required
#@duo_auth.duo_auth_required
class LocateViewSet(viewsets.ModelViewSet):
    queryset = Locate.objects.all()
    serializer_class = LocateSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id','PS_Case_ID','latitude', 'longitude','address','city','zip_code','event_date',)


class VehicleViewset(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    paginate_by = 50
    paginate_by_peram = 'page_size'
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('ID','PS_case', 'Vehicle_ID','Vehicle_Number','Make','Vehicle_Model','Travel_Direction','Vehicle_Maneuver', 'Traffic_Control_Device','Driver_Condition',)

class PersonViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    paginate_by = 50
    serializer_class = PersonSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('ID','PS_case','Sex', 'Age', 'Injury_Level', 'Status_Code', 'Person_Type',' Vehicle_Number')

class Personset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    paginate_by = 50
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('ID','PS_case','Sex', 'Age', 'Injury_Level', 'Status_Code', 'Person_Type',' Vehicle_Number')

class PViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('ID','PS_case','Sex', 'Age', 'Injury_Level', 'Status_Code', 'Person_Type','Vehicle_Number')

class ProfileViewset(viewsets.ModelViewSet):
    queryset = up.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields =('ID','PS_case','Vehicle_Number','Person_Type','Safety_Equip','State_Reside','Sex','Full_Name','Age')

class uvViewset(viewsets.ModelViewSet):
    queryset = uv.objects.all()
    serializer_class = uvSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('ID','PS_case','Vehicle_Number','MV_Body')

class ucfViewset(viewsets.ModelViewSet):
    queryset = uc.objects.all()
    serializer_class = UCFCSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('ID','PS_case','Assigned_Crash_Record','DLD_Year', 'DLD', 'County_Code', 'Route', 'Date_of_Crash', 'Manner_Collision','Roadway_Contrib_Circum','Weather_Condition', 'First_Harmful_Event', 'Narrative')


#DELETE

@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def delete_up(request, pk):
    aa = request.session['del']
    post = get_object_or_404(up, pk=pk).delete()
    return redirect('uc-edit', pk=aa)

@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def delete_uc(request, pk):
    post = get_object_or_404(uc, pk=pk).delete()
    return redirect('u')

@user_passes_test(lambda u: u.groups.filter(name= 'QC').count() == 1)
def delete_uv(request, pk):
    aa = request.session['del']
    post = get_object_or_404(uv, pk=pk).delete()
    return redirect('uc-edit', pk=aa)

