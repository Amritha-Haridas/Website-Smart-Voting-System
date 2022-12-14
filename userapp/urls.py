from django.urls import path
from . import views

urlpatterns = [
    path('',views.user,name='user'),
    path('about/',views.about,name='about'),
    path('getDetails/',views.getDetails,name='getDetails'),
    path('getitem/',views.getitem,name='getitem'),
    path('uslogin/',views.uslogin,name='uslogin'),
    path('uservote/',views.uservote,name='uservote'),
    path('uservoteview/',views.uservoteview,name='uservoteview'),
    path('vote/<int:did>/',views.vote,name='vote'),
    path('voteresult/',views.voteresult,name='voteresult'),
    path('greeting/<face_id>/',views.Greeting,name='greeting'),
    path('contact/',views.contact,name='contact'),
    path('getmethod/',views.getmethod,name='getmethod'),
    path('userlogout/',views.userlogout,name='userlogout')
]