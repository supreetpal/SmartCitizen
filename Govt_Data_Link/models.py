from django.db import models

# Create your models here.

class Political_Party(models.Model):
    name                =  models.TextField(null=True,blank=True)
    cp                  =  models.TextField(null=True,blank=True)   #Chairperson
    pl_cp               =  models.TextField(null=True,blank=True)   #Parliamentary Chairperson
    ldr_lok_sabha       =  models.TextField(null=True,blank=True)   #Leader in Lok Sabha
    ldr_raj_sabha       =  models.TextField(null=True,blank=True)   #Leader in Rajya Sabha
    founded_on          =  models.TextField(null=True,blank=True)   
    preceded_by         =  models.TextField(null=True,blank=True)
    headquaters         =  models.TextField(null=True,blank=True)
    newspaper           =  models.TextField(null=True,blank=True)
    youth_wing          =  models.TextField(null=True,blank=True)
    women_wing          =  models.TextField(null=True,blank=True)
    pol_position        =  models.TextField(null=True,blank=True)   #Political Position
    colors              =  models.TextField(null=True,blank=True)
    eci_status          =  models.TextField(null=True,blank=True)
    alliance            =  models.TextField(null=True,blank=True)
    seats_lok_sabha     =  models.IntegerField(null=True,blank=True)   # out of 545
    seats_raj_sabha     =  models.IntegerField(null=True,blank=True)   # out of 245
   
    

class Year_of_Ruling(models.Model):
    party               = models.ForeignKey(Political_Party,null=True)
    pm                  = models.TextField(null=True,blank=True)
    took_office         = models.DateTimeField(null=True,blank=True)
    left_office         = models.DateTimeField(null=True,blank=True)
    
