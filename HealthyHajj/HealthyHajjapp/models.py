from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Delegation(models.Model):
    MAX_LEN_COUNTRY = 36
    MAX_LEN_AGENCY = 100
    Country = models.TextField(max_length= MAX_LEN_COUNTRY)
    Agency = models.TextField (max_length= MAX_LEN_AGENCY )


# Create your models here.
class Doctor (models.Model):
    MAX_LENGTH_SPECIALTY = 40

    Specialty =  models.TextField(max_length= MAX_LENGTH_SPECIALTY)
    Localisation = models.DecimalField ( max_digits=8, decimal_places=3 )

class HajjParticipant (models.Model):
    B_Type = (('A','A+'),('B','B+'),('O','O+'),('AB','AB+'),('A','A-'),('B','B-'),('O','O-'),('AB','AB-'))

    Birthday = models.DateTimeField()
    Bloodtype = models.TextField(choices=B_Type)



class MedicalHistory (models.Model):

    Date  = models.DateTimeField ()
    Description = models.TextField()



class Ilness (models.Model) :

    TransferMethode =  (('B','Blood'),('A','AIR'),('O','Other'))
    Name = models.TextField()
    Contageous = models.BooleanField()
    Transfarabilty = models.TextField(choices=TransferMethode)
    Description  = models.TextField()