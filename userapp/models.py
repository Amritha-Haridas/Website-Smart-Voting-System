from django.db import models

# Create your models here.
class Contactdb(models.Model):
    cname=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
    phone=models.IntegerField()
    message=models.TextField(max_length=30)