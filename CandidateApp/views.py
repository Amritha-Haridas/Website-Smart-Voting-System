from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from Adminapp . models import *
from userapp . models import *
from Face_Detection.models import *

# Create your views here.
def chome(request):
    data = Candidatedb.objects.filter(status=1)
    candidate_count = Candidatedb.objects.filter(status=1).count()
    voters_count = Profile.objects.all().count()
    return render(request,'chome.html',{'data':data,'candidate_count':candidate_count,'voters_count':voters_count})

def cregister(request):
    return render(request,'cregister.html')

def getDatas(request):
    if request.method=="POST":
        candidateid=request.POST.get('candidateid')
        candidatename=request.POST.get('candidatename')
        partyname=request.POST.get('partyname')
        membersprt=request.POST.get('membersprt')
        age=request.POST.get('age')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        photo=request.FILES['photo']
        logo=request.FILES['logo']
        username=request.POST.get('username')
        password=request.POST.get('password')
        data =  Candidatedb(candidateid=candidateid,candidatename=candidatename,partyname=partyname, membersprt=membersprt,age=age,email=email, phone=phone,address=address,photo=photo, logo=logo,username=username,password=password)
        data.save()
        return redirect('cregister')

def clogin(request):
    return render(request,'clogin.html')

def getitems(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Candidatedb.objects.filter(username=username,password=password).exists():
            data = Profile.objects.filter(username=username,password=password).values('id','candidateid','candidatename','partyname','membersprt','age','email','phone','address','photo,''logo').first()
            request.session['id'] = data['id']
            request.session['candidateid'] = data['candidateid']
            request.session['candidatename'] = data['candidatename']
            request.session['partyname'] = data['partyname']
            request.session['membersprt'] = data['membersprt']
            request.session['age'] = data['age']
            request.session['email'] = data['email']
            request.session['phone'] = data['phone']
            request.session['address'] = data['address']
            request.session['photo'] = data['photo']
            request.session['logo'] = data['logo']
            request.session['username'] = username
            request.session['password'] = password
            return redirect('loginhome')
        else:
            return render(request,'clogin.html',{'msg':'Invalid user credentials'})  
    else:
        return render(request,'clogin.html',{'msg':'Invalid user credentials'})      

def clogout(request):
    del request.session['id']
    del request.session['candidatename']
    del request.session['partyname']
    del request.session['membersprt']
    del request.session['age']
    del request.session['email']
    del request.session['phone']
    del request.session['address']
    del request.session['photo']
    del request.session['logo']
    del request.session['uname']
    del request.session['pass']
    return redirect('chome')

def contact1(request):
     return render(request,'contact1.html')

def getmessage(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        num = request.POST.get('phone')
        message = request.POST.get('message')
        data = Candidatecontactdb(name=name,email=email,phone=num,message=message)
        data.save()
        return redirect('contact1')
    

def getmethod(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        num = request.POST.get('phone')
        message = request.POST.get('message')
        data = Contactdb(name=name,email=email,phone=num,message=message)
        data.save()
        return redirect('contact')

def viewcandidate(request):
    data=Candidatedb.objects.filter(status=1)
    return render(request,'viewcandidate.html',{'data':data})

def delete(request,did):
    Candidatedb.objects.filter(id=did).delete()
    return redirect('viewcandidate')

def candidate_edit(request,did):
    data = Candidatedb.objects.filter(id=did)
    return render(request,'candidate_edit.html',{'data':data})

def update1(request,did):
    if request.method=="POST":
        candidateid=request.POST.get('candidateid')
        candidatename=request.POST.get('candidatename')
        partyname=request.POST.get('partyname')
        membersprt=request.POST.get('membersprt')
        age=request.POST.get('age')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
   
    try:
            img_c = request.FILES['photo']
            img_e = request.FILES['logo']
            fs = FileSystemStorage()
            file1 = fs.save(img_c.name, img_c)
            file2 = fs.save(img_e.name, img_e)
    except MultiValueDictKeyError:
            file1 = Candidatedb.objects.get(id=did).photo
            file2 = Candidatedb.objects.get(id=did).logo
    Candidatedb .objects.filter(id=did).update(candidateid=candidateid,candidatename=candidatename,partyname=partyname, membersprt=membersprt,age=age,email=email, phone=phone,address=address,photo=file1, logo=file2)
    return redirect('viewtable') 

def loginhome(request):
     return render(request,'loginhome.html')



