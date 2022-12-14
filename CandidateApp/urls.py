from django.urls import path
from . import views

urlpatterns = [
    path('chome/',views.chome,name='chome'),
    path('cregister/',views.cregister,name='cregister'),
    path('clogin/',views.clogin,name='clogin'),
    path('getitems/',views.getitems,name='getitems'),
    path('clogout/',views.clogout,name='clogout'),
    path('contact1/',views.contact1,name='contact1'),
    path('getDatas/',views.getDatas,name='getDatas'),
    path('viewcandidate/',views.viewcandidate,name='viewcandidate'),
    path('delete/<int:did>/',views.delete,name='delete'),
    path('candidate_edit/<int:did>/',views.candidate_edit,name='candidate_edit'),
    path('update1/<int:did>/',views.update1,name='update1'),
    path('getmessage/',views.getmessage,name='getmessage'),
    path('loginhome/',views.loginhome,name='loginhome')









]
    