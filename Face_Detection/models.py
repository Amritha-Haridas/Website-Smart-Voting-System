from email.policy import default
from django.db import models

class UserProfile(models.Model):
    face_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length = 100,default='')
    email = models.CharField(max_length = 20,default='')
    username = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=10,default='')
    def __str__(self):
        return self.name

class Profile(models.Model):
    face_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50,default='')
    address = models.CharField(max_length = 100,default='')
    email = models.CharField(max_length = 30,default='')
    phone = models.CharField(max_length = 30,default='')
    place = models.CharField(max_length = 30,default='')
    username = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=10,default='')
    date = models.DateField(default='2000-12-02')