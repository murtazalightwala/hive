from datetime import date
from django.contrib.auth.models import User
from django.contrib.gis.db import models as gmodels
from djongo import models as dmodels


# Create your models here.

class Patient(dmodels.Model):
    Gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other','Other'),
    ]

    Relationship_status_choices = [
        ('married', 'Married'),
        ('unmarried','Unmarried'),
    ]

    user = dmodels.OneToOneField(User, on_delete=dmodels.CASCADE)
    dob = dmodels.DateField(default = date.today)
    gender = dmodels.CharField(choices = Gender_choices, max_length=10)
    relationship_status = dmodels.CharField(choices = Relationship_status_choices, max_length= 20)
    children = dmodels.IntegerField()
    address = dmodels.CharField(max_length= 400)
    profession = dmodels.CharField(max_length= 20)
    blood_group = dmodels.CharField(max_length= 10)
    height = dmodels.CharField(max_length= 10)
    weight = dmodels.CharField(max_length= 10)
    blood_pressure = dmodels.CharField(max_length= 20)
    allergies = dmodels.CharField(max_length= 200)
    sugar_level = dmodels.CharField(max_length= 20)
    routine_medications = dmodels.CharField(max_length= 200)
    surgical_history = dmodels.CharField(max_length= 200)
    other_details = dmodels.CharField(max_length= 200)
    em_contact_name = dmodels.CharField(max_length= 100)
    em_phone = dmodels.CharField(max_length= 20)
    is_in_healthcare = dmodels.BooleanField()
    healthcare_catagory = dmodels.CharField(max_length= 20)



class Drug(dmodels.Model):
    drug_id = dmodels.IntegerField(primary_key = True)
    drug_name = dmodels.CharField(max_length = 50)

class Drugstock(dmodels.Model):
    drugstock_id = dmodels.IntegerField(primary_key = True)
    drug = dmodels.IntegerField()
    rate = dmodels.FloatField()
    stock = dmodels.IntegerField() 

class Pharmacy(dmodels.Model):
    
    phar_id = dmodels.IntegerField(primary_key = True)
    name = dmodels.CharField(max_length = 250)
    address = dmodels.CharField(max_length=600)
    geolocation = gmodels.PointField()
    inventory = dmodels.ArrayField(model_container = Drugstock)

class Doctor(dmodels.Model):
    
    doctor_id = dmodels.IntegerField(primary_key = True)
    name = dmodels.CharField(max_length = 250)
    address = dmodels.CharField(max_length=600)
    image_url = dmodels.CharField(max_length = 600)

class PrescribedDrug(dmodels.Model):
    
    pd_id = dmodels.IntegerField(primary_key = True)
    pd = dmodels.EmbeddedField(model_container = Drug)
    count = dmodels.IntegerField()
    frequency = dmodels.IntegerField()
    duration = dmodels.IntegerField()

class Prescription(dmodels.Model):
    
    prescription_id = dmodels.IntegerField(primary_key = True)
    doctor = dmodels.OneToOneField(Doctor, on_delete=dmodels.CASCADE)
    date = dmodels.DateField()
    mode = dmodels.CharField(max_length = 200)
    details = dmodels.CharField(max_length = 600)

    prescription_drug_list = dmodels.ArrayField(model_container = PrescribedDrug)

