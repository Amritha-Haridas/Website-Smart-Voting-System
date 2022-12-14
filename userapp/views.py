from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from Adminapp . models import *
from Face_Detection.models import *
from Face_Detection.detection import FaceRecognition
import datetime
from django.contrib import messages
from django.db.models.aggregates import Max

faceRecognition = FaceRecognition()

# Create your views here.
def user(request):
      data = Candidatedb.objects.filter(status=1)
      candidate_count = Candidatedb.objects.filter(status=1).count()
      voters_count = Profile.objects.all().count()
      return render(request,'user.html',{'data':data,'candidate_count':candidate_count,'voters_count':voters_count})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def getmethod(request):
    if request.method=="POST":
        cname = request.POST.get('cname')
        email = request.POST.get('email')
        num = request.POST.get('phone')
        message = request.POST.get('message')
        data = Contactdb(cname=cname,email=email,phone=num,message=message)
        data.save()
        return redirect('contact')

def getDetails(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        place = request.POST.get('place')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print(age)
        face_id = request.POST.get('face_id')
        data1=Profile(face_id=face_id,name=name,email=email,password=password,username=username,address=address,age=age,phone=phone,place=place,gender=gender)
        data1.save()

        addFace(request.POST.get('face_id'))
        return redirect('user')
    else:
        return HttpResponse("Not Registered")

def addFace(face_id):
    face_id = face_id
    faceRecognition.faceDetect(face_id)
    faceRecognition.trainFace()
    return redirect('user')

def uslogin(request):
    return render(request,'uslogin.html')

def getitem(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Profile.objects.filter(username=username,password=password).exists():
            data = Profile.objects.filter(username=username,password=password).values('face_id','name','email','age','phone','place').first()
            request.session['id'] = data['face_id']
            request.session['name'] = data['name']
            request.session['email'] = data['email']
            request.session['age'] = data['age']
            request.session['phone'] = data['phone']
            request.session['place'] = data['place']
            request.session['uname'] = username
            request.session['pass'] = password
            face_id = faceRecognition.recognizeFace()
           
            return redirect('greeting' ,str(face_id))
        else:
            return render(request,'uslogin.html',{'msg':'Invalid user credentials'})  
    else:
        return redirect('uslogin')

def Greeting(request,face_id):
    face_id = int(face_id)
    data1 = Profile.objects.filter(face_id = face_id)
    data = Candidatedb.objects.all()
    return render(request,'faceDetection/greeting.html',{'data1':data1,'data':data})

def uservote(request):
    data=Candidatedb.objects.filter(status=1)
    return render(request,'uservote.html',{'data':data})

def uservoteview(request,did):
    data = Candidatedb.objects.all()
    return render(request,'uservote.html',{'data':data})
 
def vote(request,did):
    face_id  = request.session.get('id')
    print(face_id)
    date = datetime.datetime.now()
    
    if Profile.objects.filter(face_id=face_id,date=date).exists():
        return HttpResponse("Already voted")
    else:
        print("Did : ",did)
        x = Candidatedb.objects.filter(id=did).values('vote')
        for i in x:
            count = i['vote']
        print(count)
        Candidatedb.objects.filter(id=did).update(vote=count+1)
        date = datetime.datetime.now()
        Profile.objects.filter(face_id=face_id).update(date=date)
        messages.success(request,'Voted Successfully')
        return redirect('user')

def voteresult(request):
    data =  Candidatedb.objects.all().aggregate(Max('vote'))
    x = data['vote__max']
    print(x)
    data =  Candidatedb.objects.filter(vote=x,status=1)
    return render(request,'voteresult.html',{'data':data})


def userlogout(request):
    del request.session['id']
    del request.session['name']
    del request.session['email']
    del request.session['age']
    del request.session['uname']
    del request.session['pass']
    return redirect('user')

