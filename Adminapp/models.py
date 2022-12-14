from django.db import models

# Create your models here.
class Candidatedb(models.Model):
    candidateid = models.IntegerField()
    candidatename = models.CharField(max_length=20)
    partyname = models.CharField(max_length=20)
    membersprt = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=30)
    photo = models.ImageField(upload_to = 'Image',default = "null.jpg")
    logo = models.ImageField(upload_to = 'Image',default = "null.jpg")
    username = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=20,default='')
    vote = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
  






