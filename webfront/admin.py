from django.contrib import admin
from webfront import models
from .forms import SignUpForm, MP
from models import SignUp, Crash, Vehicle,Person, Locate,uc

# Register your models here.


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    form = SignUpForm

#class PostA(admin.ModelAdmin):
#    list_display = ['PS_case','ID','user', 'Date_of_Crash']

#admin.site.register(Crash, PostA)
admin.site.register(Crash)
admin.site.register(Locate)
admin.site.register(Vehicle)
admin.site.register(Person)
admin.site.register(uc)

