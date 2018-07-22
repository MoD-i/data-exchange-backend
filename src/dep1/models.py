from django.db import models

# Create your models here.


class Scheme(models.Model):
    
    FEMALE = 'F'
    MALE = 'M'
    TRANS = 'T'
    GENDER_CHOICES = ((FEMALE, 'Female'), (MALE, 'Male'), (TRANS, 'Transgender'))

    aadhar_number = models.CharField(max_length=15, unique=True, primary_key=True)
    beneficiary_name = models.CharField(max_length = 50, null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, null=True, blank=True)
    member_age =  models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    dist_name = models.CharField(max_length=50, null=True, blank=True)
    scheme_name = models.CharField(max_length=100, null=True, blank=True)


class Ticket(models.Model):
    ticket_id = models.IntegerField(primary_key=True, unique=True)
