from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('addcandidate/',views.addcandidate,name='addcandidate'),
    path('getData/',views.getData,name='getData'),
    path('viewtable/',views.viewtable,name='viewtable'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adlogin/',views.adlogin,name='adlogin'),
    path('adlogout/',views.adlogout,name='adlogout'),
    path('vote_result/',views.vote_result,name='vote_result'),
    path('viewregister/',views.viewregister,name='viewregister'),
    path('viewcontact/',views.viewcontact,name='viewcontact'),
    path('approve/<int:did>/',views.approve,name='approve'),
    path('delete1/<int:did>/',views.delete1,name='delete1'),
    path('approvecandidate/',views.approvecandidate,name='approvecandidate'),
    path('viewcandidatecontact/',views.viewcandidatecontact,name='viewcandidatecontact')


    

    
]
