from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from Face_Detection . models import *
from userapp . models import *
from CandidateApp . models import *
from django.db.models.aggregates import Max
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    c_count = Candidatedb.objects.all().count()
    v_count = Profile.objects.all().count()
    return render(request,'index.html',{'c_count':c_count,'v_count':v_count})

def addcandidate(request):
    return render(request,'addcandidate.html')    

def getData(request):
    if request.method=="POST":
        cid=request.POST.get('cid')
        cname=request.POST.get('cname')
        party=request.POST.get('pname')
        member=request.POST.get('msupport')
        age=request.POST.get('age')
        email=request.POST.get('email')
        no=request.POST.get('number')
        address=request.POST.get('address')
        photo=request.FILES['photo']
        logo=request.FILES['logo']
        data =  Candidatedb(candidateid=cid,candidatename=cname,partyname=party, membersprt=member,age=age,email=email, phone=no,address=address,photo=photo, logo=logo)
        data.save()
        return redirect('addcandidate')

def viewtable(request):
    data=Candidatedb.objects.filter(status=0)
    return render(request,'viewtable.html',{'data':data})



def adminlogin(request):
    return render(request,'adlogin.html')

def adlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username_a'] = username
            request.session['password_a'] = password
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('adminlogin')
    else:
        return render(request, 'adlogin.html')

def adlogout(request):
    del request.session['username_a']
    del request.session['password_a']
    return redirect('adminlogin')

def vote_result(request):
    data =  Candidatedb.objects.all().aggregate(Max('vote'))
    x = data['vote__max']
    print(x)
    data =  Candidatedb.objects.filter(vote=x,status=1)
    print(data)
    return render(request,'vote_result.html',{'data':data})

def viewregister(request):
    data = Profile.objects.all()
    return render(request,'viewregister.html',{'data':data})

def viewcontact(request):
    data = Contactdb.objects.all()
    return render(request,'viewcontact.html',{'data':data})

def viewcandidatecontact(request):
    data = Candidatecontactdb.objects.all()
    return render(request,'viewcandidatecontact.html',{'data':data})

def approvecandidate(request):
    data = Candidatedb.objects.filter(status=1)
    return render(request,'approvecandidate.html',{'data':data})

def approve(request,did):
    data = Candidatedb.objects.filter(id=did).update(status=1)
    return redirect('viewtable')

def delete1(request,did):
    Candidatedb.objects.filter(id=did).delete()
    return redirect('viewtable')









