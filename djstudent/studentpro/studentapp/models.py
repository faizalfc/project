from django.db import models

class studata1(models.Model):
    Student_Name=models.CharField(max_length=25, blank=False, null=False)
    Student_Dept=models.CharField(max_length=20, blank=False, null=False)
    Age=models.IntegerField()
    Mobile=models.BigIntegerField()
    Email=models.EmailField(max_length=55)
class subjects(models.Model):
    
    Student_Name=models.CharField(max_length=20,blank=False, null=False)
    Mark1=models.IntegerField()
    Mark2=models.IntegerField()
    Mark3=models.IntegerField()
    Mark4=models.IntegerField()
