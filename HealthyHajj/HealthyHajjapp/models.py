from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Delegation(models.Model):
    def __init__ (self) :
        pass
    MAX_LEN_COUNTRY = 36
    MAX_LEN_AGENCY = 100
    Country = models.TextField(null= True, max_length= MAX_LEN_COUNTRY , default=None )
    Agency = models.TextField (null = True , max_length= MAX_LEN_AGENCY )

# Create your models here.


class Doctor (models.Model):

    MAX_LENGTH_SPECIALTY = 40
    Name = models.TextField(null = True , default= None )
    Specialty =  models.TextField(null = True , max_length= MAX_LENGTH_SPECIALTY)
    Localisation = models.DecimalField ( max_digits=8, decimal_places=3 )


class HajjParticipant (models.Model):

    B_Type = (('A','A+'),('B','B+'),('O','O+'),('AB','AB+'),('A','A-'),('B','B-'),('O','O-'),('AB','AB-'))
    name = models.TextField(default= None)
    Birthday = models.DateTimeField()
    Bloodtype = models.TextField(null = True, choices=B_Type, default= None )

    Delegation = models.ForeignKey('Delegation',
                                   on_delete=models.SET_NULL,
                                   related_name='Belongs',
                                   null= True)



class MedicalHistory (models.Model):

    Date  = models.DateTimeField ()
    Description = models.TextField(default= None )
    Patient = models.ForeignKey ('HajjParticipant',
                                 on_delete=models.SET_NULL,
                                 null=True)
    Showcase = models.ManyToManyField('Ilness')



class Ilness (models.Model) :


    TransferMethode =  (('B','Blood'),('A','AIR'),('O','Other'))
    Name = models.TextField(null= True, default= None )
    Contageous = models.BooleanField(default= False)
    Transfarabilty = models.TextField(null = True , choices=TransferMethode, default= None )
    Description  = models.TextField(null = True, default = None )
