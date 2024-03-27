from django.db import models

# Create your models here.
class News(models.Model):
    noccation=models.TextField()
class Holidays(models.Model):
    date=models.DateField()
    occation=models.TextField()    

class Employee(models.Model):
    ename=models.CharField(max_length=60)
    eid=models.IntegerField()
    edes=models.TextField()
    edate=models.CharField(max_length=50)
    edept=models.TextField()
    esal=models.FloatField()
    eexp=models.IntegerField()




