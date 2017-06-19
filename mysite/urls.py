"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from webfront.views import home, contact, about, form, dyno, profile, full, u, duo
from rest_framework import routers
from rest_framework.routers import DefaultRouter
admin.autodiscover()
router = DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
#    url(r'^contact/$', contact,name='contact'),
    url(r'^about/$', about, name='about'),
    url(r'^form/$',form, name='form'),
                          
#  Authenticated:
    url(r'^search/',dyno, name='search'),
    url(r'^full/',full),
#    url(r'^fullc/','webfront.views.fullc'),
    url(r'^u/',u),
#    url(r'^c/','webfront.views.c', name='cmv'),
    url(r'^accounts/profile/$', profile,name='profile'),
                                                             
# GIS
#   url(r'^map/$', 'webfront.views.imap', name='map'),
#   url(r'^imap/$', 'webfront.views.imap', name='imap'),
#   url(r'^pmap/$', 'webfront.views.pmap', name='pmap'),

## Rest API
   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   url(r'^', include('webfront.urls')),
                                                                                                  
## Admin
#   url(r'^admin/', include(admin.site.urls)),
   url(r'^', include(router.urls)),
   url(r'^duo_private/',duo),
   url(r'^accounts/', include('registration.auth_urls')),
   url(r'^accounts/', include('registration.backends.default.urls')),
        
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
