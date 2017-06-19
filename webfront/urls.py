from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers, renderers
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from webfront.views import crash_detail, check_new, crash_check, checkin, crash_edit, crash_new, vehicle_new, vehicle_detail, vehicle_edit, person_new, person_detail, person_edit, geo_new, geo_edit, PostListView, PostViewSet, LocateViewSet, ListView, CMVView, PViewset, Personset, VehicleViewset, ProfileViewset, ucfViewset, uc_edit, uce , uv_new, up_new, delete_uc, delete_uv, delete_up, uc_new, audit, chore, ca, va, pa, auditframe, ucfcrash, ucfveh, ucfper, geo_rest, conflicts, cc, cv, cp, reconcile_crash, reconcile_vehicle, reconcile_person, delete_cc, delete_cv, delete_cp, contact

import duo_auth

from .models import Crash, Locate, Vehicle, Person, uc, up, uv, conflict_crash, conflict_vehicle, conflict_person, CrashAudit, VehicleAudit, PersonAudit

 
#basic = PostViewSet.as_view({
#    'get': 'list',
#    'post': 'create'
#})

router = routers.SimpleRouter()
router.register(r'queryfield', PostViewSet)
router.register(r'queryall', PostListView)
router.register(r'queryit', LocateViewSet)
router.register(r'query', ListView)
router.register(r'queryc', CMVView)
router.register(r'pepSPLAJOHKCTZG905A', PViewset)
router.register(r'que', Personset)
router.register(r'veh57RGJI@UBWV4FOCN', VehicleViewset)
router.register(r'pro', ProfileViewset)
router.register(r'r', ucfViewset)

urlpatterns = [
           url(r'^api/', include(router.urls)),
           url(r'^api-token-auth/', obtain_jwt_token),
           url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
           url(r'accounts/duo_login/$', duo_auth.login, name='duo_login'),
           url(r'accounts/duo_logout/$', duo_auth.logout),


#            url(r'^api-token-auth/', obtain_jwt_token),
#            url(r'^restricted/$', RestrictedView.as_view()),
#QC GROUP   
            url(r'^contact/$', contact, name='contact'),
            url(r'^crash/(?P<pk>[0-9]+)/$', crash_detail, name='crash_detail'),
            url(r'^crash/check/new/$', check_new, name='check_new'),
            url(r'^crash/(?P<pk>[0-9]+)/check/$', crash_check, name='crash_check'),
            url(r'^crash/(?P<pk>[0-9]+)/checkin/$', checkin, name='crash_checkin'),
            url(r'^crash/(?P<pk>[0-9]+)/edit/$', crash_edit, name='crash_edit'),
            url(r'^crash/new/$', crash_new, name='crash_new'),
            url(r'^vehicle/new/$', vehicle_new, name='vehicle_new'),
            url(r'^vehicle/(?P<pk>[0-9]+)/$', vehicle_detail, name='vehicle_detail'),
            url(r'^vehicle/(?P<pk>[0-9]+)/edit/$', vehicle_edit, name='vehicle_edit'),
            url(r'^person/new/$', person_new, name='person_new'),
            url(r'^person/(?P<pk>[0-9]+)/$', person_detail, name='person_detail'),
            url(r'^person/(?P<pk>[0-9]+)/edit/$', person_edit, name='person_edit'),
#GIS
            url(r'^g/$',geo_new, name='geo-new'),
            url(r'^g/(?P<pk>[0-9]+)/edit/$', geo_edit, name='geo-edit'),
            url(r'^gup/(?P<pk>[0-9]+)/edit/$', geo_rest, name='geo-rest'),
#UNCONFIRMED
#            url(r'^loc',views.loc.as_view(), name='loc'),
            url(r'^uc/$', uc_new, name='uc-new'),
            url(r'^uc/(?P<pk>[0-9]+)/$', ucfcrash.as_view(), name='uc-detail'),
            url(r'^uc/(?P<pk>[0-9]+)/edit/$', uc_edit, name='uc-edit'),
            url(r'^uce/(?P<pk>[0-9]+)/edit/$', uce, name='uce'),
            url(r'^up/(?P<pk>[0-9]+)/$', ucfper.as_view(), name='up-detail'),
            url(r'^uv/(?P<pk>[0-9]+)/$', ucfveh.as_view(), name='uv-detail'),
            url(r'^uv/new/$', uv_new, name='uv-new'),
            url(r'^up/new/$', up_new, name='up-new'),
#DELETE
            url(r'^delete/(?P<pk>\d+)/uc/$', delete_uc, name='delete_uc'),
            url(r'^delete/(?P<pk>\d+)/uv/$', delete_uv, name='delete_uv'),
            url(r'^delete/(?P<pk>\d+)/up/$', delete_up, name='delete_up'),
	    url(r'^delete/(?P<pk>\d+)/cc/$', delete_cc, name='delete_cc'),
	    url(r'^delete/(?P<pk>\d+)/cv/$', delete_cv, name='delete_cv'),
	    url(r'^delete/(?P<pk>\d+)/cp/$', delete_cp, name='delete_cp'),
#AUDIT
            url(r'^audit/$',audit, name='audit'),
            url(r'^chore/$',chore, name='chore'),
            url(r'^crash/(?P<pk>[0-9]+)/audit/$', ca, name='audit-crash'),
            url(r'^vehicle/(?P<pk>[0-9]+)/audit/$', va, name='audit-vehicle'),
            url(r'^person/(?P<pk>[0-9]+)/audit/$', pa, name='audit-person'),
            url(r'^auditframe/$',auditframe, name='auditframe'),
#Conflicts

            url(r'^conflict/$',conflicts, name='conflict'),
	    url(r'^crash/(?P<pk>[0-9]+)/conflict/$', cc, name='conflict-crash'),
	    url(r'^vehicle/(?P<pk>[0-9]+)/conflict/$', cv, name='conflict-vehicle'),
	    url(r'^person/(?P<pk>[0-9]+)/conflict/$', cp, name='conflict-person'),

    	    url(r'^rc/(?P<pk>[0-9]+)/edit/$', reconcile_crash, name='reconcile_crash'),
            url(r'^rv/(?P<pk>[0-9]+)/edit/$', reconcile_vehicle, name='reconcile_vehicle'),
	    url(r'^rp/(?P<pk>[0-9]+)/edit/$', reconcile_person, name='reconcile_person'),



#            format_suffix_patterns([
#                url(r'^api/', api_root),
#                url(r'queryfield', basic, name='queryfield'),
#            ])
            ]
#urlpatterns = format_suffix_patterns(urlpatterns)
